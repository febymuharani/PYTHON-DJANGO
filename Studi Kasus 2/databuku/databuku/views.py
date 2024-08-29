from django.views.generic import TemplateView
from cerpen.views import CerpenPerKategori
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogHomeView(TemplateView, CerpenPerKategori):
    template_name = "index.html"

    

    def get_context_data(self):
        queryset = self.get_latest_cerpen_each_kategori()
        context = {
            'latest_cerpen_list':queryset
        }

        return context
    