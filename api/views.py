# views.py
from rest_framework import generics
from .models import Branch, Student, Lecture
from .serializers import BranchSerializer, StudentSerializer, LectureSerializer

class BranchListView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class LectureListView(generics.ListCreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
