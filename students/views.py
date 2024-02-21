from django.shortcuts import render
from django.http.response import HttpResponse
from students.models import Student

# Create your views here.


def students_view(request):
    texto = ("<html>"
             "Hola Mundo dede una variable"
             "</html>")

    return HttpResponse(texto)


def students_list_view(request):
    students = Student.objects.all()
    context = {"students":students}
    return render(request, "students/list.html", context=context)
