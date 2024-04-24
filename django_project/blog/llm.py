from .models import Post, Resume
from .forms import ResumeForm
from django.views import View
from blog import views
from django.contrib.auth.models import User
import torch

from transformers import T5Tokenizer, T5ForConditionalGeneration

def getSummary(post_contents):
    summary = [ ]
    model_name = "sarahai/ruT5-base-summarizer"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    device = torch.device("cpu")  # if you are using cpu
    for post_content in post_contents:
        input_text = post_content  # concatenate all posts into a single string
        input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to(device)
        outputs = model.generate(input_ids, max_length=100, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
        sum = tokenizer.decode(outputs[0], skip_special_tokens=True)
        summary.append(sum)
        
    return summary
  