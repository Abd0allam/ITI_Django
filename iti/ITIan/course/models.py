from django.db import models


class Course(models.Model):
    name= models.CharField(max_length=50)
    Duration=models.IntegerField()

    def __str__(self) :
        return self.name
