from django.urls import path
from .views import student_list, student_add

urlpatterns = [
    path('', student_list, name='student_list'),
    path("add/", student_add, name="student_add"),
]
