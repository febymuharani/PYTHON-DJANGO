from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from .models import Artikel
from .forms import ArtikelForm

# Create your views here.

class ArtikelFormView(FormView):
    form_class = ArtikelForm
    template_name =  'blog/create.html'
    #success_url = '/blog/all/'
    success_url = reverse_lazy('blog:list', kwargs={'penulis': 'all'})
    extra_context = {
        'page_title' : 'Create Artikel'
    }

    def get_context_data(self,*args,**kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args,**kwargs)

    def form_valid(self, form):
        #print(form.cleaned_data)
        form.save()
        return super().form_valid(form)


class ArtikelDetailView(DetailView):
    model = Artikel
    extra_context = {
         'page_title' : 'Detail Artikel'
    }

    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)

        artikel_lain = self.model.objects.exclude(slug=self.kwargs['slug'])
        self.kwargs.update({'artikel_lain' : artikel_lain})

        kwargs = self.kwargs
        print(kwargs)
        return super().get_context_data(*args,**kwargs)





class ArtikelListView(ListView):
    model = Artikel
    ordering = ['update']
    #paginate_by = 2
    extra_context = {
        'page_title' : 'Blog List'
    }
    

    def get_queryset(self):
        if self.kwargs['penulis'] != 'all':
            self.queryset = self.model.objects.filter(penulis__iexact = self.kwargs['penulis'])
            self.kwargs.update({'penulis':self.kwargs['penulis'],})
        return super().get_queryset()



    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)

