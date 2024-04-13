from django import forms
from .models import Resume

GENDER_CHOICES = [
 ('Male', 'Male'),
 ('Female', 'Female')
]

JOB_CITY_CHOICE = [
 ('AL', 'Alabama'), 
 ('AZ', 'Arizona'), 
 ('AR', 'Arkansas'), 
 ('CA', 'California'), 
 ('CO', 'Colorado'), 
 ('CT', 'Connecticut'), 
 ('DE', 'Delaware'), 
 ('DC', 'District of Columbia'), 
 ('FL', 'Florida'), 
 ('GA', 'Georgia'), 
 ('ID', 'Idaho'), 
 ('IL', 'Illinois'), 
 ('IN', 'Indiana'), 
 ('IA', 'Iowa'), 
 ('KS', 'Kansas'), 
 ('KY', 'Kentucky'), 
 ('LA', 'Louisiana'), 
 ('ME', 'Maine'), 
 ('MD', 'Maryland'), 
 ('MA', 'Massachusetts'), 
 ('MI', 'Michigan')
]

class ResumeForm(forms.ModelForm):
 gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
 job_city = forms.MultipleChoiceField(label='Preferred Job Locations', choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)
 class Meta:
  model = Resume
  fields = ['name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_file', 'blog']
  labels = {'name':'Full Name', 'dob': 'Date of Birth', 'locality': 'Street Address', 'pin':'Pin Code', 'mobile':'Mobile No.', 'email':'Email ID', 'profile_image':'Profile Image', 'my_file':'Document', 'blog': 'My blog post'}
  widgets = {
   'name':forms.TextInput(attrs={'class':'form-control'}),
   'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
   'locality':forms.TextInput(attrs={'class':'form-control'}),
   'city':forms.TextInput(attrs={'class':'form-control'}),
   'pin':forms.NumberInput(attrs={'class':'form-control'}),
   'state':forms.Select(attrs={'class':'form-select'}),
   'mobile':forms.NumberInput(attrs={'class':'form-control'}),
   'email':forms.EmailInput(attrs={'class':'form-control'}),
  }