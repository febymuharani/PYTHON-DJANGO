from django import forms


class ContactForm(forms.Form):
    nama_lengkap       = forms.CharField(max_length=10)


    GENDER = (
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan')
    )
    jenis_kelamin      = forms.ChoiceField(
                            widget= forms.RadioSelect,
                            choices= GENDER)
    

    TAHUN = range(2000,2030,1)
    tanggal_lahir = forms.DateField(
                            widget= forms.SelectDateWidget(years=TAHUN)
                            )

    email              = forms.EmailField(label='Alamat Email')

    alamat             = forms.CharField(
                            widget= forms.Textarea,
                            max_length=100, 
                            required=False)
    
    agree              = forms.BooleanField()