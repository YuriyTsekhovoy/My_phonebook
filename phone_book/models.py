from django.db import models

# Create your models here.


class SignName(models.Model):
    sign_name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.sign_name


class PhoneNumber(models.Model):
    name = models.ForeignKey(SignName)
    number = models.CharField('Phone Number', max_length=15)
    is_mobile = models.BooleanField('Mobile', default=True)
