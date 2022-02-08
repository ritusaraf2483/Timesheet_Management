from datetime import date

from django.db import models
from django.urls import reverse

from usermanagement.models import User


class Location(models.Model):
    location=models.CharField(max_length=20)

    def __str__(self):
         return self.location

class Workday(models.Model):
     id=models.IntegerField(primary_key=True)
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     location=models.ForeignKey(Location,on_delete=models.CASCADE)
     sector=models.CharField(max_length=10)
     work_date=models.DateField(default=date.today)
     time_in=models.TimeField()
     time_out=models.TimeField()
     hours_code=models.CharField(max_length=10)
     FBP_payroll=models.FloatField() # Only one type of payroll per workday.. You may want to define it as a different entity 
     AMCO_payroll=models.FloatField()

     def get_absolute_url(self):
          return reverse('Workday:workday_list')
