from django.db import models
import eav
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = PhoneNumberField(blank=True)

    def __str__(self):
        return self.name

eav.register(Contact)
