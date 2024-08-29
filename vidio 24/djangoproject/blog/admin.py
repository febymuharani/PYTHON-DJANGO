from django.contrib import admin

# Register your models heref

from .models import Post

class Postadmin(admin.ModelAdmin):
    readonly_fields = ['slug']

admin.site.register(Post, Postadmin)