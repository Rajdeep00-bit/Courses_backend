from rest_framework import serializers
from .models import Course, CourseInstance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseInstance
        fields = ['course', 'year', 'semester']  # Ensure these match the model's fields

    def validate(self, data):
        # Add custom validation if needed
        if not data.get('course'):
            raise serializers.ValidationError("Course is required.")
        if not data.get('year'):
            raise serializers.ValidationError("Year is required.")
        if not data.get('semester'):
            raise serializers.ValidationError("Semester is required.")
        return data

