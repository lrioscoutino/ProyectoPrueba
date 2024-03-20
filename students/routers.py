from rest_framework import routers
from students.viewsets import StudentsViewsets

router = routers.DefaultRouter()

router.register(
    'students',
    StudentsViewsets
)