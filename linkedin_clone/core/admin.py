from django.contrib import admin

from .models import CustomUser, UserProfile, Education, Certification, Course, Experience, Follow, Notification

admin.site.site_header = 'LinkedIn Clone'


class ModelAdminCustomUser(admin.ModelAdmin):
    """Addresses admin for Customuser Model."""
    list_display = [
        'id', 'first_name', 'last_name', 'username', 'email',
        'date_joined', 'is_active', 'is_staff', 'created_at', 'updated_at'
    ]
    search_fields = ['username', 'email']
    ordering = ['date_joined']
    list_filter = ['is_superuser']

admin.site.register(CustomUser, ModelAdminCustomUser)


class ModelAdminUserProfile(admin.ModelAdmin):
    """Addresses admin for UserProfile Model."""

    list_display = ['id', 'user', 'industry', 'website', 'phone_number', 'birthdate', 'location']
    search_fields = ['user', 'location']
    ordering = ['-created_at']
    list_filter = ['age']

admin.site.register(UserProfile, ModelAdminUserProfile)


class ModelAdminEducation(admin.ModelAdmin):
    """Addresses admin for Customuser Model."""

    list_display = [
        'id', 'user', 'school', 'degree', 'field_of_study', 'start_date',
        'end_date', 'grade', 'description', 'skills', 'media'
    ]
    ordering = ['-created_at']

admin.site.register(Education, ModelAdminEducation)


class ModelAdminExperience(admin.ModelAdmin):
    """Admin for Experience Model."""

    list_display = [
        'id', 'user', 'title', 'employment_type', 'company_name', 'location',
        'location_type', 'start_date', 'description', 'skills', 'media'
    ]
    ordering = ['-created_at']
    list_filter = ['employment_type', 'location_type']

admin.site.register(Experience, ModelAdminExperience)


class ModelAdminCertification(admin.ModelAdmin):
    """Admin for Certification Model."""

    list_display = [
        'id', 'user', 'name', 'issuing_organization', 'issue_date',
        'expiration_date', 'credential_id', 'credential_url'
    ]
    ordering = ['-created_at']
    list_filter = ['issue_date']

admin.site.register(Certification, ModelAdminCertification)


class ModelAdminCourse(admin.ModelAdmin):
    """Admin for Course Model."""

    list_display = ['id', 'user', 'course_name', 'course_code', 'associated_with']
    ordering = ['-created_at']

admin.site.register(Course, ModelAdminCourse)


class ModelAdminFollow(admin.ModelAdmin):
    """Admin for Follow model."""

    list_display = ['id', 'follower', 'following']

admin.site.register(Follow, ModelAdminFollow)


class ModelAdminNotifications(admin.ModelAdmin):
    """Admin for Notifications model."""

    list_display = ['id', 'receiver', 'message', 'is_read']

admin.site.register(Notification, ModelAdminNotifications)
