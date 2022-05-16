from django.db import models


# Create your models here.
class Data(models.Model):
    heading = models.CharField(max_length=50)
    description = models.TextField()
    imgUrl = models.CharField(max_length=250)
