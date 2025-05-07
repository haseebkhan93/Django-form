from django.db import models



class Info(models.Model):
        name = models.TextField(max_length=200,verbose_name="Full name")
        email =models.EmailField(verbose_name="Email Address", unique=True)
        age = models.IntegerField(verbose_name="Age")
        gender = models.TextField(max_length=10, choices= [("Male","Male"),("Female","Female")])
        country = models.TextField(max_length=100,verbose_name= "Country")
# Create your models here.

        def __str__(self):
            return self.name
