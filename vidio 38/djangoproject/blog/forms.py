from django import forms


from .models import PostModel
 

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = [
            'author',
            'judul',
            'body',
            'category',
        ]

        labels = {
            'author' : 'Penulis'
        }

        widgets = {
            'judul': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder' : 'Isi Judul Yang Kamu Mau'
                }
            ),
            'author': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder' : 'Silahkan Isi Nama Penulis'
                }
            ),
            'body': forms.Textarea(
                attrs= {
                    'class':'form-control',
                }
            ),
            'category': forms.Select(
                attrs= {
                    'class':'form-control',
                }
            ),
        }
