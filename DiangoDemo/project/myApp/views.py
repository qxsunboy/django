from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Grades,Students


def index(request):
    return HttpResponse("sunck is a good man!")


def detail(request):
    return HttpResponse("ddd")

def grades(request):
    gradesList=Grades.objects.all()
    return  render(request,'myApp/grades.html',{"gradeList":gradesList})
