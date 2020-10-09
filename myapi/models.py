from django.db import models
from django.contrib.auth.models import User
# Create your models here.

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


class Data(models.Model):
    name = models.CharField(max_length=200, null=False)
    category = models.CharField(max_length=200, choices=category_names)

    def __str__(self):
        return self.name

    objects = models.Manager()


class SaveFile(models.Model):
    data = models.ForeignKey(Data, blank=True, null=True, on_delete=models.CASCADE)
    file = models.FileField(upload_to='temp/', blank=True, null=True)

    def __str__(self):
        return '%s' % (str(self.data) + '/' + str(self.file.name))

    objects = models.Manager()