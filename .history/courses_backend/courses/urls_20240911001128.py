from django.urls import path
from .views import CourseListCreate, CourseDetail, CourseInstanceListCreate, CourseInstanceDetail

urlpatterns = [
    # Courses URLs
    path('api/courses/', views.CourseListCreate.as_view(), name='course-list-create'),
    path('api/courses/<int:pk>/', views.CourseDetail.as_view(), name='course-detail'),
    
    # Course Instances URLs
    path('api/instances/', views.CourseInstanceListCreate.as_view(), name='course-instance-list-create'),
    path('api/instances/<int:year>/<int:semester>/', views.CourseInstanceListCreate.as_view(), name='course-instance-list'),
    path('api/instances/<int:year>/<int:semester>/<int:pk>/', views.CourseInstanceDetail.as_view(), name='course-instance-detail'),
   
]
