from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Ustoz

def body_funk(request):
    return HttpResponse("Tamom")

def add_student(request):
    student = Student()
    student.name = "Bunyod"
    student.group = "315"
    student.age = 27
    student.save()
    return HttpResponse("qushdik")

def student_list(request):
    students = Student.objects.all()
    for student in students:
        print(students)
    return HttpResponse("Student List")

def add_ustoz(request):
    student = Ustoz()
    student.name = "Bunyod"
    student.surname = "Usmonov"
    student.age = 27
    student.save()
    return HttpResponse("qushdik")

def ustoz_list(request):
    students = Ustoz.objects.all()
    for student in students:
        print(students)
    return HttpResponse("Student List")
