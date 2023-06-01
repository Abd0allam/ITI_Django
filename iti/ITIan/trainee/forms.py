from django import forms
from .models import trainee
from course.models import Course
        
class Traineeform(forms.ModelForm):
    class Meta:
        model=trainee
        fields='__all__'


class Courseform(forms.ModelForm):
    class Meta:
        model=Course
        fields=('name',)