from django.urls import path
from .views import index
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_required(index.as_view()),name="index"),
    # path('addstudent/', login_required(addStudent.as_view()),name="addStudent")
]
