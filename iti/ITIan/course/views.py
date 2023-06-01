from django.shortcuts import render
from django.http import HttpResponse
from .models  import Course

def index(request):
    course=Course.objects.all()
    context={'courses':course }
    return render(request ,'course/course.html',context)
