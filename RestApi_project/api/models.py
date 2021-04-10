from django.db import models

# Create your models here
class Employee(models.Model):
    fullname = models.CharField(max_length=20)
    emp_code = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.fullname