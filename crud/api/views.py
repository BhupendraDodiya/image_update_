from django.shortcuts import render
from rest_framework import generics
from .serializers import StudentSerializer
from app.models import Student

# Create your views here.
class Registration(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class rud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer