from django.db import models

# Create your models here.
class DoctorReg(models.Model):
    pname = models.CharField(max_length=100)
    pemail = models.CharField(max_length=100)
    pphone = models.CharField(max_length=100)
    paddress = models.TextField()
    password = models.CharField(max_length=100)
    doctor=models.BooleanField(default=False)

class predictions(models.Model):
    age = models.IntegerField()
    sex = models.IntegerField()
    cp = models.IntegerField()
    trestbps = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.IntegerField()
    restecg = models.IntegerField()
    thalach = models.IntegerField()
    exang = models.IntegerField()
    oldpeak = models.IntegerField()
    slope = models.IntegerField()
    ca = models.IntegerField()
    thal = models.IntegerField()
    target = models.IntegerField()