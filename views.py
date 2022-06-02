from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.db.models import Q
from django.views.generic import *
import time

from Main.models import Coffee

@cache_page(60 * 10)
def index(request):
    time.sleep(100)
    return render(request, 'index.html')

@cache_page(60 * 9)
def about(request):
    time.sleep(100)
    return render(request, 'about.html')

@cache_page(60 * 8)
def blog(request):
    time.sleep(100)
    return render(request, 'blog.html')

@cache_page(60 * 7)
def contact(request):
    time.sleep(100)
    return render(request, 'contact.html')

def payment(request):
    return render(request, 'payment.html')

def order(request):
    return render(request, 'order.html')

# def cafestore(request):
#     return render(request, 'cafe view.html')


class CafeListView(ListView):
    model = Coffee
    template_name = 'cafe view.html'

    def get_context_data(self):
        q = Coffee.objects.all()
        time.sleep(10)
        url_dict = self.request.GET
        if 'search-text' in url_dict and url_dict['search-text']:
            text = url_dict.get('search-text')
            q = q.filter(Q(name__icontains=text))

        context = {'coffees': q}
        return context


class CafeCreateView(CreateView):
    model = Coffee
    fields = ['name', 'description', 'price', 'image']
    template_name = 'cafe create.html'
    success_url = '../view/'


class CafeUpdateView(UpdateView):
    model = Coffee
    fields = ['name', 'description', 'price', 'image']
    template_name = 'cafe update.html'
    success_url = '../view/'

    def get_object(self):
        return Coffee.objects.get(pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.object.id
        return context


class CafeDeleteView(DeleteView):
    model = Coffee
    template_name = 'cafe delete.html'
    success_url = '../view/'