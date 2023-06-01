from django.db import models
from course.models import Course

class trainee(models.Model):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    age=models.IntegerField()
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.first_name +" " + self.last_name

