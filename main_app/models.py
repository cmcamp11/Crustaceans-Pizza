from django.db import models
from django.urls import reverse

# Create your models here.

class Topping(models.Model):
  name = models.CharField(max_length=50)
  qty = models.IntegerField(default=1)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toppings_detail', kwargs={'pk': self.id})

class Pizza(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  qty = models.IntegerField(default=1)
  toppings = models.ManyToManyField(Topping)

  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'pizza_id': self.id})

