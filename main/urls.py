from django.urls import path
from .views import student_list, student_add, student_edit, student_delete

urlpatterns = [
    path("", student_list, name="student_list"),
    path("add/", student_add, name="student_add"),
    path("edit/<int:pk>/", student_edit, name="student_edit"),
    path("delete/<int:pk>/", student_delete, name="student_delete"),
]
