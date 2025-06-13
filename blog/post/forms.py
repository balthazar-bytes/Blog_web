from django import forms
<<<<<<< HEAD
from .models import Avatar
=======

>>>>>>> 20035d3c1acf975ef2bd9fa1a9ef42ebb18dc217

from .models import Post


class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'autor', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
<<<<<<< HEAD
        }
        
        
class AvatarForm(forms.Form):
    class Meta:
        model = Avatar
        fields = ['imagen']
        
        
=======
        }
>>>>>>> 20035d3c1acf975ef2bd9fa1a9ef42ebb18dc217
