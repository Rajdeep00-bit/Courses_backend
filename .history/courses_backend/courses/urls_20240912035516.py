from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name='course-detail'),
    
    path('instances/', views.CourseInstanceListCreate.as_view(), name='course-instance-list-create'),
    path('instances/<int:pk>/', views.CourseInstanceDetail.as_view(), name='course-instance-detail'),
    
    path('', views.home, name='home'),
]
