from django.db import models
from django.contrib.auth.models import User as user



class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)
# Create your models here.

class Avatar(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares/', blank=True, null=True)