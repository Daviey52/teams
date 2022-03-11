from django.db import models
from django.contrib.auth import get_user_model

class Teams(models.Model):
  name = models.CharField(max_length=64)
  trophy = models.TextField(default='')
  rater= models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

  def __str__(self):
    return self.name
