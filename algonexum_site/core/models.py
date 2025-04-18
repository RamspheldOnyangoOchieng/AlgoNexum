from django.db import models

# Create your models here.


class User(models.Model):
    fullname = models.CharField(max_length=254)
    email = models.EmailField(unique=True,max_length=254)
    password = models.CharField(max_length=254)
    def __str__(self):
        return self.fullname
    