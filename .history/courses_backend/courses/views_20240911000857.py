from rest_framework import generics
from django.http import Http404, HttpResponse  
from django.shortcuts import get_object_or_404
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

# Courses
class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Course Instances
class CourseInstanceListCreate(generics.ListCreateAPIView):
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        """
        Return a list of course instances filtered by year and semester, if provided.
        Otherwise, return all course instances.
        """
        queryset = CourseInstance.objects.all()
        year = self.kwargs.get('year')
        semester = self.kwargs.get('semester')
        
        if year and semester:
            queryset = queryset.filter(year=year, semester=semester)
        return queryset

class CourseInstanceDetail(generics.RetrieveDestroyAPIView):
    serializer_class = CourseInstanceSerializer

    def get_object(self):
        """
        Get a course instance filtered by course ID, year, and semester.
        Raise 404 if the object does not exist.
        """
        return get_object_or_404(
            CourseInstance, 
            course__id=self.kwargs['pk'],
            year=self.kwargs['year'], 
            semester=self.kwargs['semester']
        )

# Home view
def home(request):
    return HttpResponse("Welcome to the Courses API! Access the endpoints via /api/courses or /api/instances.")
