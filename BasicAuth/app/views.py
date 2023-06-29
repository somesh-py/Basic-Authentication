from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serilizers import StudentSerilizers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class StudentAPI(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerilizers
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]