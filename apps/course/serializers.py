from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class ExerciseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"


class ExercisefileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise_file
        fields = "__all__"
