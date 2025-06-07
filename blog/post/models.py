from django.db import models



class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)
# Create your models here.
