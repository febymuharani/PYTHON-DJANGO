from django import forms

from .models import Post

 # class PostForm(forms.Form):
   # judul         = forms.CharField(max_length=100)
   # body          = forms.CharField(widget=forms.Textarea)
   # category      = forms.CharField(max_lenght=100)


# IMPORT MODEL DARI MODELS.PY
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'judul',
            'body',
            'category', 
        ]
