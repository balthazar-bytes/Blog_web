from django import forms
from .models import Post
from django.urls import path
from .views import post_list,PostDetailView, PostCreateView

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
]
