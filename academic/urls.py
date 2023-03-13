from django.urls import path
from .views import index,addStudent,addClass,addSubject,editStudent,DeleteStudent
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',index.as_view(),name="index"),
    path('addstudent/', login_required(addStudent.as_view()),name="addStudent"),
    path('editstudent/<str:pk>', login_required(editStudent.as_view()),name="editStudent"),
    path('deletestudent/<str:id>', login_required(DeleteStudent.as_view()),name="deleteStudent"),

    path('addclass/',login_required(addClass.as_view()),name="addClass"),
    path('addsubject/',login_required(addSubject.as_view()),name="addSubject"),
]
