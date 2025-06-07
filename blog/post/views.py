from django.shortcuts import render
from django.conf import settings 
from .models import Post
from .forms import Postform
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView


def post_list(request):
    post = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': post})

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'
    
    
class PostCreateView(CreateView):
    model = Post
    form_class = Postform
    template_name = 'post/post_form.html'
    success_url = '/'
# Create your views here.
