from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from students.models import Student
from django.urls import reverse_lazy

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


def student_add_view(request):
    if request.method == 'POST':
        student = Student()
        student.name = request.POST['name']
        student.control_number = request.POST['control_number']
        student.semester = request.POST['semester']
        student.save()
        return redirect(reverse_lazy('student-list'))
    return render(request, "students/add.html")
