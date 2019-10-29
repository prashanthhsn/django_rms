from django.db import models


class room(models.Model):
    city = models.CharField(max_length=20)
    rent = models.IntegerField
    features = models.CharField(max_length=500)