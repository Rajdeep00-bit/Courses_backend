from rest_framework import generics, status
from rest_framework.response import Response
from django.http import Http404, HttpResponse  
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
    View to list all course instances for a specific year and semester, and create new instances.
    If year and semester are not provided, all course instances will be listed.
    """
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
    """
    View to retrieve or delete a course instance by course ID, year, and semester.
    """
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

    def delete(self, request, *args, **kwargs):
        """
        Custom delete method to handle the deletion of a course instance.
        """
        instance = self.get_object()  # Get the instance to delete
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


# Home view
def home(request):
    """
    Simple home view to return an introductory message.
    """
    return HttpResponse("Welcome to the Courses API! Access the endpoints via /api/courses or /api/instances.")
