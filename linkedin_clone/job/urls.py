from django.urls import path

from . import views

app_name = 'job'

urlpatterns = [
    path('tags/', views.TagListCreateView.as_view(), name='tag-list-create'),
    path('jobs/', views.JobPostListCreateView.as_view(), name='job-post-list-create'),
    path('jobs/<int:pk>/', views.JobPostDetailView.as_view(), name='job-post-detail'),
    path('applications/', views.JobApplicationListCreateView.as_view(), name='job-application-list-create'),
    path('applications/<int:pk>/', views.JobApplicationDetailView.as_view(), name='job-application-detail'),
]