from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy
# Create your views here.
from .models import Cerpen
from .forms import CerpenForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import IsPenulisMixin, IsPembacaMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

def is_penulis(user):
    return user.groups.filter(name='penulis').exists()



class ForbiddenView(TemplateView):
    template_name = 'forbidden.html'


class CerpenUpdateView(LoginRequiredMixin,UpdateView,IsPenulisMixin):
    form_class = CerpenForm
    model = Cerpen
    template_name = "cerpen/cerpen_update.html"

    @method_decorator(user_passes_test(is_penulis))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CerpenDeleteView(LoginRequiredMixin,DeleteView,IsPenulisMixin):
    model = Cerpen
    template_name = "cerpen/cerpen_delete.html" # Pakai Delete Confirmation
    success_url = reverse_lazy('cerpen:manage')

    @method_decorator(user_passes_test(is_penulis))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CerpenManageView(LoginRequiredMixin,ListView,IsPembacaMixin):
    model = Cerpen
    template_name = "cerpen/cerpen_manage.html"
    context_object_name = 'cerpen_list'
    
    


class CerpenCreateView(LoginRequiredMixin,CreateView,IsPenulisMixin):
    form_class = CerpenForm
    template_name = "cerpen/cerpen_create.html"

    
    @method_decorator(user_passes_test(is_penulis))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CerpenPerKategori():
    model = Cerpen

    def get_latest_cerpen_each_kategori(self):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        queryset = []

        for kategori in kategori_list:
            cerpen = self.model.objects.filter(kategori=kategori).latest('published')
            queryset.append(cerpen)

        return queryset



class CerpenKategoriView(ListView):
    model = Cerpen
    template_name = "cerpen/cerpen_kategori.html"
    context_object_name = 'cerpen_list'
    ordering = ['-published']
    paginate_by = 3

    def get_queryset(self):
        self.queryset = self.model.objects.filter(kategori=self.kwargs['kategori'])
        return super().get_queryset()
    
    def get_context_data(self, *args, **kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct().exclude(kategori=self.kwargs['kategori'])
        self.kwargs.update({'kategori_list':kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(*args,**kwargs)


class CerpenListView(LoginRequiredMixin,ListView):
    model = Cerpen
    template_name = "cerpen/cerpen_list.html"
    context_object_name = 'cerpen_list'
    ordering = ['-published']
    paginate_by = 3


    def get_context_data(self, *args, **kwargs,):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list':kategori_list})
        kwargs = self.kwargs


        return super().get_context_data(*args,**kwargs)


class CerpenDetailView(DetailView):
    model = Cerpen
    template_name = "cerpen/cerpen_detail.html"
    context_object_name = 'cerpen'



    def get_context_data(self, *args, **kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list':kategori_list})

        cerpen_serupa = self.model.objects.filter(kategori=self.object.kategori).exclude(id=self.object.id)
        self.kwargs.update({'cerpen_serupa':cerpen_serupa})
        kwargs = self.kwargs


        return super().get_context_data(*args,**kwargs)