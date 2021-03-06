from django.db import models
from datetime import datetime


import json


# Create your models here.
class DType(models.Model):
  dtype = models.CharField(max_length=12, unique=True)
  mode = models.CharField(max_length=12, default="spent")

  def __str__(self):
    return self.dtype


class Data(models.Model):
  #spent or profit
  mode = models.CharField(max_length=12, default="spent")
  value = models.FloatField(blank=False, null=False)
  date = models.DateField()
  dtype = models.ForeignKey(DType, on_delete=models.PROTECT)
  description = models.TextField(null=True)


  def get_date(self):
    return self.date.strftime("%d/%m/%y")

  
  def get_value(self):
    return "{:,.2f}".format(self.value)
    

