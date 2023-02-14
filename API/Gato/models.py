from django.db import models

# Create your models here.


class Usuario(models.Model):
    Id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=20)

class Gatito(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    Gato = models.ImageField(null=True)