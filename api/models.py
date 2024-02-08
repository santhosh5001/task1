# models.py
from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=255)

class Student(models.Model):
    name = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

class Lecture(models.Model):
    name = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
