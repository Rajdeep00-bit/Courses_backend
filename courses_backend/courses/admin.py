from django.contrib import admin
from .models import Course, CourseInstance

# Registering the Course model
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_code')
    search_fields = ('title', 'course_code')

# Registering the CourseInstance model
@admin.register(CourseInstance)
class CourseInstanceAdmin(admin.ModelAdmin):
    list_display = ('course', 'year', 'semester')
    search_fields = ('course__title', 'year', 'semester')
    list_filter = ('year', 'semester')
