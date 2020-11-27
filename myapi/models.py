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


class Contacts(models.Model):
    cont_fname = models.CharField(max_length=200, null=True)
    cont_lname = models.CharField(max_length=200, null=True)
    cont_company = models.CharField(max_length=200, null=True)
    cont_phone = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    objects = models.Manager()

class Tags(models.Model):

    objects = models.CharField(max_length=200, null=True)
    categories = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
        return self.get_category_display()

    objects = models.Manager()

class Data(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=20, null=True)
    value = models.DateField(max_length=200, null=True)
    initials = models.CharField(max_length=200, null=True)
    contact = models.ForeignKey(Contacts, blank=True, null=True, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, blank=True, null=True, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name
    #     return self.get_category_display()
    #
    # objects = models.Manager()



class Appartments(models.Model):
    appartment_name = models.CharField(max_length=200, null=True)
    floor = models.CharField(max_length=200, null=True)

class Zones(models.Model):
    number = models.CharField(max_length=100, primary_key=True)
    appartment = models.ForeignKey(Appartments, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    finishing = models.CharField(max_length=50, null=True)
    height = models.CharField(max_length=50, null=True)
    surface = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Properties(models.Model):
    guid = models.CharField(max_length=50, primary_key=True)
    related_zone = models.ForeignKey(Zones, blank=True, null=True, on_delete=models.CASCADE)
    related_doc = models.ForeignKey(Data, blank=True, null=True, on_delete=models.CASCADE)
    elem_id = models.CharField(max_length=50, null=True)
    serial_number = models.CharField(max_length=50, null=True)
    producer = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    quantity = models.CharField(max_length=50, null=True)
    production_date = models.CharField(max_length=50, null=True)
    warranty_date = models.CharField(max_length=50, null=True)
    price = models.CharField(max_length=50, null=True)
    website = models.CharField(max_length=50, null=True)




class SaveFile(models.Model):
    file = models.FileField(upload_to='files/', blank=True, null=True)
    data = models.ForeignKey(Data, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (str(self.data) + '/' + str(self.file.name))

    # @property
    # def relative_path(self):
    #     return os.path.relpath(self.path, settings.MEDIA_ROOT)

    objects = models.Manager()