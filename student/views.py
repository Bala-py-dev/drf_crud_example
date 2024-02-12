from django.shortcuts import render
from rest_framework import generics
from student.models import StudentDetail
from student.serializers import StudentDetailSerializer

# Create your views here.

class StudentDetailListCreate(generics.ListCreateAPIView):
    queryset = StudentDetail.objects.all()
    serializer_class = StudentDetailSerializer

class StudentDetailRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentDetail.objects.all()
    serializer_class = StudentDetailSerializer
    lookup_field = 'id'
