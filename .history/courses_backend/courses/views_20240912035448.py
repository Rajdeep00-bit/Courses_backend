from rest_framework import generics, status
from rest_framework.response import Response
from django.http import HttpResponse  
from django.shortcuts import get_object_or_404
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

# Courses
class CourseListCreate(generics.ListCreateAPIView):
    """
    View to list all courses and create a new course.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveDestroyAPIView):
    """
    View to retrieve or delete a specific course by ID.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# Course Instances
class CourseInstanceListCreate(generics.ListCreateAPIView):
    """
    View to list all course instances or create a new course instance.
    Supports optional filtering by year and semester.
    """
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        """
        Return a list of course instances filtered by year and semester, if provided.
        Otherwise, return all course instances.
        """
        queryset = CourseInstance.objects.all()
        year = self.request.query_params.get('year')
        semester = self.request.query_params.get('semester')
        
        if year and semester:
            queryset = queryset.filter(year=year, semester=semester)
        return queryset


class CourseInstanceDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve or delete a specific course instance by ID.
    """
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

    def get_object(self):
        """
        Override to fetch CourseInstance by ID.
        """
        return get_object_or_404(CourseInstance, id=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        """
        Override to delete a specific course instance by ID.
        """
        instance = self.get_object()  # Fetch the instance by ID
        self.perform_destroy(instance)  # Perform the deletion
        return Response(status=status.HTTP_204_NO_CONTENT)


# Home view
def home(request):
    """
    Simple home view to return an introductory message.
    """
    return HttpResponse("Welcome to the Courses API! Access the endpoints via /api/courses or /api/instances.")
