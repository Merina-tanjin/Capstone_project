from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.template import loader
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from .forms import ResumeForm
from .models import Resume
from django.views import View
from .llm import getSummary

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



class HomeView(View):
   
    def get(self, request):
      form = ResumeForm()
      candidates = Resume.objects.all()
      return render(request, 'blog/resume_home.html', { 'candidates':candidates, 'form':form})

    def post(self, request):
      form = ResumeForm(request.POST, request.FILES)
      
      if form.is_valid():
         form.save()

      return redirect('resume_home')

class CandidateView(View):
   
   def get(self, request, **kwargs):
      pk = kwargs['pk']
      candidates = Resume.objects.get(pk=pk)
      user = User.objects.get(username=candidates.name)  
      posts = Post.objects.filter(author=user).order_by('-date_posted')

      post_contents = [post.content for post in posts]
      post_contents = post_contents[:5]
      summary = getSummary(post_contents)

      return render(request, 'blog/candidate.html', {'candidate':candidates, 'posts': summary})



