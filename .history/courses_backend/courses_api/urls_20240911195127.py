from django.contrib import admin
from django.urls import path, include
from courses.views import home

urlpatterns = [
    path('', home),  # Root URL now shows a simple welcome message.
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),
  
]
