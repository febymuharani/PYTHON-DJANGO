from django.contrib import admin

# Register your models here.
from .models import Cerpen

class CerpenAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'updated',
        'published',
    ]


admin.site.register(Cerpen,CerpenAdmin)