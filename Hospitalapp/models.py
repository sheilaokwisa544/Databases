from django.db import models
# handles databases


# Create your models here.
class patient(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField()
    contact = models.IntegerField()
    def __str__(self):
        return self.name

class appointment(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    department = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    message = models.TextField()
    def __str__(self):
        return self.name


