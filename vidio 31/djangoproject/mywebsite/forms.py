from django import forms

class FormField(forms.Form):
    
    # python data type
    integer_field                = forms.IntegerField(required=False) # maka dia boleh tidak di isi
    decimal_field                = forms.DecimalField(required=False)
    float_field                  = forms.FloatField(required=False)
    boolean_field                = forms.BooleanField(required=False)
    char_field                   = forms.CharField(max_length=10, required=False) 
    #max_length=10    # maka haya 10 karakter yang bisa di isi

    # String Input
    email_field 		= forms.EmailField(required=False)
    regex_field = forms.RegexField(regex=r'(?P<test>)')
    slug_field			= forms.SlugField()
    url_field			= forms.URLField()
    ip_field			= forms.GenericIPAddressField()

    # Select Input
    PILIHAN = {
        ('nilai1', 'pilihan1'),
        ('nilai2', 'pilihan2'),
        ('nilai3', 'pilihan3'),
    }
    choice_field               = forms.ChoiceField(choices=PILIHAN)
    multi_choice_field         = forms.MultipleChoiceField(choices=PILIHAN)
    multi_typed_field          = forms.TypedMultipleChoiceField(choices=PILIHAN)
    null_boolean_field         = forms.NullBooleanField()

    # Date Time
    date_field                    = forms.DateField()
    datetime_field                = forms.DateTimeField()
    duration_field                = forms.DurationField()
    time_field                    = forms.TimeField()
    splitdatetime_field           = forms.SplitDateTimeField()


    # File Input
    file_field             = forms.FileField()
    image_field            = forms.ImageField()








