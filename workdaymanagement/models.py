from datetime import date

from django.db import models
from django.urls import reverse


class Location(models.Model):
    location=models.CharField(max_length=20)

    def __str__(self):
         return self.location

class Workday(models.Model):
     fileno=models.IntegerField(primary_key=True)
     user=models.CharField(max_length=20)
     location=models.ForeignKey(Location,on_delete=models.CASCADE)
     sector=models.CharField(max_length=10)
     work_date=models.DateField(default=date.today)
     time_in=models.TimeField()
     time_out=models.TimeField()
     hours_code=models.CharField(max_length=10)
     FBP_payroll=models.FloatField()
     AMCO_payroll=models.FloatField()

     def get_absolute_url(self):
          return reverse('Workday:workday_list')