from django.urls import path
from .views import CourseListCreate, CourseDetail, CourseInstanceListCreate, CourseInstanceDetail

urlpatterns = [
    # Course List and Create (Ensure Trailing Slash)
   path('api/courses/', CourseListCreate.as_view(), name='course-list-create'),
    path('api/courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
]
    # Course Instances List/Create and Filtered by year and semester
    path('api/instances/', CourseInstanceListCreate.as_view(), name='course-instance-list-create'),
    path('api/instances/<int:year>/<int:semester>/', CourseInstanceListCreate.as_view(), name='course-instance-list-year-semester'),
    path('api/instances/<int:year>/<int:semester>/<int:pk>/', CourseInstanceDetail.as_view(), name='course-instance-detail'),
]
