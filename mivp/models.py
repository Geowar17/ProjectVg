from django.db import models
from django.contrib.auth.models import User
# Creatde your models here.

class Projects(models.Model):
    name= models.CharField(max_length=200)
    name_contacto=models.CharField(max_length=200)
    number_contacto=models.CharField(max_length=20)
    mail= models.EmailField()
    direction_contac= models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    

class Stage(models.Model):
    name = models.CharField(max_length=100)
    default_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name



class Tasks(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Baja'),
        ('medium', 'Media'),
        ('high', 'Alta'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



