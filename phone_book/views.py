from django.shortcuts import render, get_list_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import SignName, PhoneNumber
from .forms import NumberForm, SignForm

# Create your views here.


def sign_list(request):
    signs = SignName.objects.all()
    return render(request, 'phone_book/sign_list.html', {'signs': signs})


def sign_detail(request, pk):
    name = SignName.objects.get(id=pk)
    sign = PhoneNumber.objects.filter(name_id=pk)
    return render(request, 'phone_book/sign_detail.html', {'sign': sign, 'name': name})


def sign_new(request):
    if request.method == "POST":
        form = SignForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('sign_detail', pk=post.pk)
    else:
        form = SignForm()
    return render(request, 'phone_book/sign_edit.html', {'form': form})

'''
def phone_new(request):
    if request.method == "POST":
        form = NumberForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('sign_detail', pk=post.pk)
    else:
        form = NumberForm()
    return render(request, 'ph_book/sign_detail.html', {'form': form})
'''


def sign_edit(request, pk):
    #post = get_list_or_404(Phone_Number, name_id)
    #name = Sign_Name.objects.get(id=pk)
    if request.method == "POST":
        form = NumberForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = SignName.objects.get(id=pk)
            post.save()
            return redirect('sign_detail', pk)
    else:
        form = NumberForm()
    return render(request, 'phone_book/number_edit.html', {'form': form})


def sign_delete(request, pk):
    sign = SignName.objects.get(id=pk)
    sign.delete()
    return redirect('sign_list')

def sign_copy(request, pk):
    sign = SignName.objects.get(id=pk)
    sign.save()
    return redirect('sign_list')
