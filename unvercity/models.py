from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100,null=False)
    group = models.CharField(max_length=50,null=False)
    age = models.SmallIntegerField(null=False)

    def __str__(self):
        return self.name

class Ustoz(models.Model):
    name = models.CharField(max_length=100,null=False)
    surname = models.CharField(max_length=50,null=False)
    age = models.SmallIntegerField(null=False)

    def __str__(self):
        return self.name

