from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jobs (models.Model):
    image = models.BinaryField()
    summary = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'works_jobs'