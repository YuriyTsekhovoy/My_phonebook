from django.views import generic

from .models import SignName, PhoneNumber
from .forms import NumberForm

# Create your views here.


class IndexView(generic.ListView):
    model = SignName
    template_name = 'phone_book/index.html'
    context_object_name = 'sign_list'


class DetailView(generic.ListView):
    model = SignName
    template_name = 'phone_book/detail.html'
    context_object_name = 'numbers'

    def get_queryset(self):
        return SignName.objects.get(id=self.kwargs['pk'])


class EditNumberView(generic.CreateView):
    model = PhoneNumber
    fields = ['name', 'number', 'is_mobile']
    #form_class = NumberForm
    template_name = 'phone_book/edit.html'
    success_url = '/'


class DelView(generic.DeleteView):
    model = SignName
    success_url = '/'


class NewSignView(generic.CreateView):
    model = SignName
    fields = ['sign_name']
    success_url = '/'
