from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudentSerializer,TeacherSerializer
from .models import Student
from .models import Teacher



# Create your views here.
@api_view(["POST"])
def postStudent(request):
    try:
        request_data = request.data
        serializer = StudentSerializer(data=request_data,many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response({"message":"I am done for Today"})
    except Exception as e:
        return Response({"err": str(e)})
@api_view(["POST"])   
def postTeacher(request):
    try:
        request_data = request.data
        serializer = TeacherSerializer(data=request_data,many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response({"message":"I am done"})
    except Exception as e:
           return Response({"err": str(e)})
    
@api_view(["GET"])  
def getStudent(request):
    students = Student.objects.all()
    serialized_data = StudentSerializer(students,many=True)
    return Response(serialized_data.data)
@api_view(["GET"])  
def getTeacher(request):
    students = Teacher.objects.all()
    serialized_data = TeacherSerializer(students,many=True)
    return Response(serialized_data.data)
        

@api_view(["GET"])
def getsingleStudentData(requests,id):
     students = Student.objects.get(id=id)
     serialized_data = StudentSerializer(students,many=False)


     return Response(serialized_data.data)

@api_view(["POST"])
def editStudentData(requests,id):
    try:
        student = Student.objects.get(id=id)
        serialized_data = StudentSerializer(student,data=requests.data,many=False)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({"message":"data updated sucessfully","data":serialized_data.data})
    except Exception as e:
         return Response({"error":e})

@api_view(["GET"])
def deleteStudentData(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return Response({"message":"data deleted sucessfully"})

@api_view(["GET"])
def deleteTeachertData(request,id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return Response({"message":"data deleted sucessfully"})


    

