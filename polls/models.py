from django.db import models
from django.utils import timezone
# Create your models here.
class Problems(models.Model):
    statement=models.CharField(max_length = 2000)
    Name=models.CharField(max_length = 200)
    code=models.CharField(max_length = 2000)
    difficulty=models.CharField(max_length = 20)

class Solutions(models.Model):
    problem=models.ForeignKey(Problems,on_delete=models.CASCADE)
    verdict=models.CharField(max_length = 20)
    time=models.DateTimeField()

class Test(models.Model):
    problem=models.ForeignKey(Problems,on_delete=models.CASCADE)
    input=models.CharField(max_length = 200)
    output=models.CharField(max_length = 200)
