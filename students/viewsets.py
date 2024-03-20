from rest_framework import viewsets
from students.models import Student
from students.serializers import StudentsSerializer


class StudentsViewsets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
