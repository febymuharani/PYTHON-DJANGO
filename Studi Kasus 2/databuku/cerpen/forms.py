from django.forms import ModelForm

from .models import Cerpen


class CerpenForm(ModelForm):
    class Meta:
        model = Cerpen
        fields = [
            'judul',
            'isi',
            'kategori'
        ]