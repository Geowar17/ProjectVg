from django.db import models

# Creatde your models here.

class Projects(models.Model):
    name= models.CharField(max_length=200)
    name_contacto=models.CharField(max_length=200)
    number_contacto=models.CharField(max_length=20)
    mail= models.EmailField()
    direction_contac= models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Tasks(models.Model):
    title= models.CharField(max_length=200)
    description=models.TextField()
    project=models.ForeignKey(Projects, on_delete=models.CASCADE)
     
    def __str__(self):
        return self.title
    
