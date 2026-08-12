from django.db import models

# models of django is use for storing the data into database

class Info(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.CharField(max_length=50)
    Contact = models.CharField(max_length=50)