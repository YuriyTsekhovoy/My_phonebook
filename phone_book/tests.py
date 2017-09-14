from django.test import TestCase

from .models import PhoneNumber, SignName

# Create your tests here.


def create_sign(sign_name):
    """
    Create a sign in the phonebook with the given 'sign_name'
    """
    return SignName.objects.create(sign_name=sign_name)


def add_number(number, is_mobile=True):
    """
    Create a new number in sign with given 'number' and 'is_mobile' mark
    """
    return PhoneNumber.objects.create(number=number, is_mobile=is_mobile)


def delete_sign(sign_name):
    """
    Delete a sign in the phonebook with the given 'sign_name'
    """
    return SignName.objects.delete(sign_name=sign_name)


class SignDetailViewTests(TestCase):

    def test_
