"""
URL configuration for ProyectoPrueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from students.views import (
    students_view,
    students_list_view,
    student_add_view,
    student_update_view,
    student_delete_view,
)
from django.contrib.auth.views import LoginView, LogoutView
from students.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',students_view, name="students"),
    path('students/list/', students_list_view, name="student-list"),
    path('', LoginView.as_view(template_name="base.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('students/add/', student_add_view, name="student-add"),
    path('students/update/<int:student_id>/', student_update_view, name="student-update"),
    path('students/delete/<int:student_id>/', student_delete_view, name="student-delete"),
    path('api/',include(router.urls) )
]
