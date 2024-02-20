from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def students_view(request):
    texto = ("<html>"
             "Hola Mundo dede una variable"
             "</html>")

    return HttpResponse(texto)


def students_list_view(request):
    name = "Luis Rios"
    student_list = [1, 2 , 3, 4, 5]
    context = {"name":name, "students":student_list}
    return render(request, "base.html", context=context)
