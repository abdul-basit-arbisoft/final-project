from rest_framework import serializers

from .models import JobPost, Tag, JobApplication


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag model."""

    class Meta:
        model = Tag
        fields = '__all__'


class JobPostSerializer(serializers.ModelSerializer):
    """Serializer for Job post model."""

    class Meta:
        model = JobPost
        fields = '__all__'


class JobApplicationSerializer(serializers.ModelSerializer):
    """Serializer for Jpb Application model."""

    class Meta:
        model = JobApplication
        fields = '__all__'
