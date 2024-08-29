from django import forms


class ContactForm(forms.Form):
    nama_lengkap        = forms.CharField(
                            label= 'Nama Lengkap',
                            max_length=25,
                            widget= forms.TextInput(
                                attrs={
                                    'class':'form-control',
                                    'placeholder':'Silahkan Masukkan Nama Lengkap Anda'
                                }
                            )
                         )
    jenis_kelamin       = forms.ChoiceField(
                            widget= forms.RadioSelect(
                                attrs={
                                    'class':'form-check-input'
                                }
                            ),
                            choices=[
                                ('L', 'Laki-Laki'),
                                ('P', 'Perempuan')
                             ]
                         )
    tanggal_lahir       = forms.DateField(
                            widget= forms.SelectDateWidget(
                                years=range(2000,2031,1),
                                attrs={
                                    'class' : 'form-control','class':'col-sm-2',
                                },
                            )
                        )
    email               = forms.EmailField(
                            widget= forms.TextInput(
                                attrs={
                                    'class' : 'form-control',
                                    'placeholder': 'Silahkan Isi Email Anda'
                                }
                            )
                         )
    alamat              = forms.CharField(
                            widget=forms.Textarea(
                                attrs={
                                'class' : 'form-control',
                                'placeholder':'Silahkan Isi Alamat Lengkap Anda'
                                }
                            )
                        )
    agree               = forms.BooleanField(
                            widget= forms.CheckboxInput(
                                attrs={
                                    'class' : 'form-check-input'
                                }
                            )
                         ) 