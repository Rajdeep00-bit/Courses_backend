from rest_framework import generics
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer


# Course List and Create View
class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Course Detail View (for retrieving, updating, and deleting)
class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# CourseInstance List and Create (with optional year and semester filtering)
class CourseInstanceListCreate(generics.ListCreateAPIView):
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        queryset = CourseInstance.objects.all()
        year = self.kwargs.get('year')
        semester = self.kwargs.get('semester')
        if year and semester:
            queryset = queryset.filter(year=year, semester=semester)
        return queryset

# CourseInstance Detail View
class CourseInstanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer
