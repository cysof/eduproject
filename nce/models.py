from django.db import models

# Create your models here.

class Department(models.Model):
    course = models.CharField(max_length=60)

class Project(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    departments = models.ManyToManyField('Department', related_name='projects')

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField()
    subject = models.CharField(max_length=60)
    message = models.TextField()

    def __str__(self):
        return self.name
