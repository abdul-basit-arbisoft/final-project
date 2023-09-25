from django.contrib import admin

from .models import JobPost, Tag, JobApplication


@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    """Addresses admin for the JobPost."""
    
    list_display = ('id', 'title', 'description', 'recruiter')


@admin.register(Tag)
class JobPostAdmin(admin.ModelAdmin):
    """Addresses admin for the Tags."""
    
    list_display = ('id', 'name')


@admin.register(JobApplication)
class JobPostAdmin(admin.ModelAdmin):
    """Addresses admin for the Job Application."""
    
    list_display = ('id', 'job', 'applicant', 'cover_letter', 'resume', 'applied_at')
    search_fields = ['job']
