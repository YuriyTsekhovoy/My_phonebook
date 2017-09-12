from django.http import HttpResponse
from django.views import generic
from django.conf.urls import url

from .models import SignName, PhoneNumber
from .forms import NumberForm, SignForm
from django.urls import reverse_lazy

# Create your views here.


class IndexView(generic.ListView):
    model = SignName
    template_name = 'phone_book/index.html'
    context_object_name = 'sign_list'


class DetailView(generic.ListView):
    model = PhoneNumber
    template_name = 'phone_book/detail.html'
    context_object_name = 'numbers'
    #queryset = PhoneNumber.objects.all()

    def get_queryset(self):
        return PhoneNumber.objects.filter(name_id=self.kwargs['pk'])


class EditNumberView(generic.CreateView):
    model = PhoneNumber
    fields = ['number', 'is_mobile']
    template_name = 'phone_book/edit.html'
    success_url = '/'

class DelView(generic.DeleteView):
    model = SignName
    success_url = '/'

class NewSignView(generic.CreateView):
	model = SignName
	fields = ['sign_name']
	success_url = '/'
