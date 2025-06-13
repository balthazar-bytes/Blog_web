from django.shortcuts import render,redirect
from django.conf import settings 
from .models import Post
from .forms import Postform
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm\


def inicio(request):
    posts_recientes = Post.objects.order_by('-fecha_publicacion')[:3]
    
    context = {
        'posts': posts_recientes
    }
    return render(request, 'post/inicio.html', context)



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
    
    
class PostUpdateView(UpdateView):
    model = Post
    form_class = Postform
    template_name = 'post/post_update.html'
    success_url = '/'
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'
    success_url = '/'
# Create your views here.


def buscarPost(request):
    query = request.GET.get('q', '')
    posts = [] 
    
    if query:
        posts = Post.objects.filter(
            Q(titulo__icontains=query) | Q(contenido__icontains=query)
        ).distinct()

    context = {
        'query': query,
        'posts': posts,
    }

    return render(request, 'post/buscarPost.html', context)


'''GESTION DE AVATARES'''

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'post/inicio.html')
        else:
            return render(request, 'post/register.html', {'form': form,'mensaje':'Porfavor, corrije los errores'})
    else:
        form = UserCreationForm()
    return render(request, 'post/register.html', {'form': form})




def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                return render(request, 'post/login.html', {'form': form, 'mensaje': 'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'post/login.html', {'form': form, 'mensaje': 'Por favor, corrija los errores'})
    
    form = AuthenticationForm()
    return render(request, 'post/login.html', {'form': form})


