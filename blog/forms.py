from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # Formulaire pour la création et la modification des posts, basé sur le modèle Post.
    class Meta:
        model = Post
        fields = ['titre', 'contenu', 'statut', 'image']
