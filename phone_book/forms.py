from django import forms

from .models import PhoneNumber, SignName


class NumberForm(forms.ModelForm):

    class Meta:
        model = PhoneNumber
        fields = ('number', 'is_mobile', )


class SignForm(forms.ModelForm):

    class Meta:
        model = SignName
        fields = ('sign_name', )
