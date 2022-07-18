from email.policy import default
from django.db import models

# Create your models here.
class MedClass(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.name

class ActiveIngredient(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=40)
    reg_num = models.CharField(max_length=15)
    med_isntruction = models.TextField(max_length=2000)
    release_form = models.CharField(max_length=30)
    min_order = models.IntegerField()
    price_exw = models.DecimalField(decimal_places=2, max_digits=10)
    med_image = models.ImageField(upload_to="D:\pharmacy\static\img", default=0)
    active_ingredient = models.ManyToManyField(ActiveIngredient)
    med_class = models.ForeignKey(MedClass, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
