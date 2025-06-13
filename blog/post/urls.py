# En Blog_web/blog/post/urls.py

from django.urls import path
from .views import inicio, register, login_view, post_list, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, buscarPost
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('post/post_list', post_list, name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_confirm_delete'),
    path('buscarPost/', buscarPost, name='buscarPost'),
    path('', inicio, name='inicio'),
    path('register/', register, name='register'),
    
    path('login/', login_view, name='login'),

    path('logout/',LogoutView.as_view(next_page='inicio'), name='logout'),
]