from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    # add data
    path('add-student/',postStudent),
    path('add-teacher/',postTeacher),

    # Get data
    path("get-student/",getStudent),
    path("get-teacher/",getTeacher),

    # edit data 
    path("edit-student/<id>",getsingleStudentData),
    path("update-student/<id>",editStudentData),
    
    # Delete student data
    path("delete-student/<id>",deleteStudentData),
    path("delete-teacher/<id>",deleteTeachertData),
]
