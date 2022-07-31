from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Teams(models.Model):
  name = models.CharField(max_length=64)
  trophy = models.TextField(default='')
  rater= models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse ('teams_detail', arg=[str(self.id)])
