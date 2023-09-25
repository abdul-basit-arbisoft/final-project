from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import JobPost, Tag, JobApplication
from .serializers import JobPostSerializer, TagSerializer, JobApplicationSerializer


class TagListCreateView(generics.ListCreateAPIView):


    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

class JobPostListCreateView(generics.ListCreateAPIView):


    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated]

class JobPostDetailView(generics.RetrieveUpdateDestroyAPIView):


    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated]

class JobApplicationListCreateView(generics.ListCreateAPIView):


    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

class JobApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):


    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]
