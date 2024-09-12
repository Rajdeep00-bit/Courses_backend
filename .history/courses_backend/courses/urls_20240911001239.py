from django.urls import path
from .views import CourseListCreate, CourseDetail, CourseInstanceListCreate, CourseInstanceDetail

urlpatterns = [
    # Course-related endpoints
    path('api/courses/', CourseListCreate.as_view(), name='course-list-create'),  # Add trailing slash
    path('api/courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),  # Add trailing slash
    
    # Course Instance-related endpoints
    path('api/instances/', CourseInstanceListCreate.as_view(), name='course-instance-list-create'),  # Add trailing slash
    path('api/instances/<int:year>/<int:semester>/', CourseInstanceListCreate.as_view(), name='course-instance-list-year-semester'),  # Add trailing slash
    path('api/instances/<int:year>/<int:semester>/<int:pk>/', CourseInstanceDetail.as_view(), name='course-instance-detail'),  # Add trailing slash
]
