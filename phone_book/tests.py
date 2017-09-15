from django.test import TestCase
from django.urls import reverse
import random

from .models import PhoneNumber, SignName

# Create your tests here.


def create_sign(sign_name):
    """
    Create a sign in the phonebook with the given 'sign_name'
    """
    for i in range(1, 6):
        SignName.objects.create(sign_name=sign_name+str(i))
    pass


def add_number(name, qty):
    """
    Create a 5 new random numbers in each sign startswith given 'name' 
    """
    robots = SignName.objects.filter(sign_name__startswith=name)
    for robot in robots:
        name_id = SignName.objects.get(sign_name=robot).id
        for i in range(qty):
            PhoneNumber.objects.create(
                name_id=name_id,
                is_mobile=random.choice([True, False]),
                number='+380'+str(random.randint(100000000, 999999999)))
    pass


def delete_sign(name):
    """
    Delete a sign in the phonebook startswith given 'name'
    """
    del_sign = SignName.objects.filter(sign_name__icontains=name)
    del_sign.delete()
    pass


def delete_last_number(few):
    """
    Delete last 'few' numbers in sign
    """
    last_five_numbers = PhoneNumber.objects.order_by("-id")[:few]
    for number in last_five_numbers:
        number.delete()
    pass


class SignDetailViewTests(TestCase):

    def test_no_phonenumbers(self):
        """
        If no phonenumbers exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContailns(
            response, "No phone numbers are availabile")
        self.assertQuerysetEqual(response.context['sign_list'], [])
