from typing import Any, List, Optional, Tuple, Union
from django.contrib import admin
from django.http.request import HttpRequest

# Register your models here.

from .models import Artikel

class ArtikelAdmin(admin.ModelAdmin):
    readonly_fields = [
        'created',
        'updated',
        'published',
        'slug'
    ]

    def get_readonly_fields(self,request,obj):

        current_user = request.user

        if obj != None:
                if current_user.has_perm("blog.publish_artikel"): # Ini untuk editor
                        readonly_fields = [
                            'created',
                            'updated',
                            'published',
                            'slug'
                        ]
                        return readonly_fields
                elif current_user.has_perm("blog.add_artikel"): # Ini Untul Penulis 
                        
                        if obj.is_published:
                            # semuanya readonly
                            #return [data.name for data in ]
                            return [data.name  for data in self.model._meta.fields]
                        else:
                            readonly_fields = [
                                    'created',
                                    'updated',
                                    'is_published',
                                    'published',
                                    'slug'
                                ]
                            return readonly_fields
        else:
            readonly_fields = [
                            'created',
                            'updated',
                            'is_published',
                            'published',
                            'slug'
                        ]
            return readonly_fields  
        




admin.site.register(Artikel, ArtikelAdmin)