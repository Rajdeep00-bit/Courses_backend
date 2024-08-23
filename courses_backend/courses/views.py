from rest_framework import generics
from django.http import HttpResponse  # Add this import
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
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        year = self.kwargs.get('year')
        semester = self.kwargs.get('semester')
        if year and semester:
            return CourseInstance.objects.filter(year=year, semester=semester)
        return super().get_queryset()

class CourseInstanceDetail(generics.RetrieveDestroyAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

    def get_object(self):
        try:
            return CourseInstance.objects.get(
                course__id=self.kwargs['pk'],
                year=self.kwargs['year'],
                semester=self.kwargs['semester']
            )
        except CourseInstance.DoesNotExist:
            raise Http404

# Home view
def home(request):
    return HttpResponse("Welcome to the Courses API! Access the endpoints via /api/courses or /api/instances.")
