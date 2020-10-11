from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import User

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    objects = models.Manager()

category_names = [
    ('finance', 'finance'),
    ('technical', 'technical')
]

value_names = [
    ('finance', 'finance'),
    ('technical', 'technical')
]

class Contacts(models.Model):
    cont_fname = models.CharField(max_length=200, null=True)
    cont_lname = models.CharField(max_length=200, null=True)
    cont_company = models.CharField(max_length=200, null=True)
    cont_phone = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

    objects = models.Manager()

class Tags(models.Model):
    categories = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.name
        return self.get_category_display()

class Data(models.Model):
    name = models.CharField(max_length=200, null=True)

    category = models.CharField(max_length=20, null=True)
    value = models.DateField(max_length=200, null=True)

    contact = models.ForeignKey(Contacts, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        return self.get_category_display()

    objects = models.Manager()


class SaveFile(models.Model):
    file = models.FileField(upload_to='temp/', blank=True, null=True)
    data = models.ForeignKey(Data, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (str(self.data) + '/' + str(self.file.name))

    # @property
    # def relative_path(self):
    #     return os.path.relpath(self.path, settings.MEDIA_ROOT)

    objects = models.Manager()