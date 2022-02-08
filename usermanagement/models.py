from django.db import models

class User(models.Model): # Profile - auth user
    id=models.IntegerField(primary_key=True)
    f_name=models.CharField(max_length=20)
    l_name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images/users')

    def __str__(self):
        return self.f_name
