from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class TimeStampMixin(models.Model):
    """Abstract model to include in all other models."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser, TimeStampMixin):
    """Custom User unique by email."""

    ADMIN = 'admin'
    EMPLOYEE = 'employee'
    RECRUITER = 'recruiter'
    USER_TYPE_CHOICES = [
        (ADMIN, 'Admin'),
        (EMPLOYEE, 'Employee'),
        (RECRUITER, 'Recruiter'),
    ]

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default=EMPLOYEE)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['date_joined']

    def __str__(self):
        return self.email


class UserProfile(TimeStampMixin):
    """Contain additional information about the User."""

    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_pic = models.FileField(upload_to='Images/Profile/', blank=True, null=True)
    cover_pic = models.FileField(upload_to='Images/Cover/', blank=True, null=True)
    headline = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    industry = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=MALE)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        ordering = ['-created_at']

    def __str__(self):
        return self.user.username


class Experience(TimeStampMixin):
    """Contain experience fields about the User."""

    ON_SITE = "on_site"
    HYBRID = "hybrid"
    REMOTE = "remote"
    LOCATION_TYPE_CHOICES = [
        (ON_SITE, "On Site"),
        (HYBRID, "Hybrid"),
        (REMOTE, "Remote"),
    ]

    FULL_TIME = 'full_time'
    PART_TIME = 'part_time'
    FREELANCE = 'freelance'
    INTERNSHIP = 'internship'
    EMPLOYMENT_TYPE_CHOICES = [
        (FULL_TIME, 'Full time'),
        (PART_TIME, 'Part Time'),
        (FREELANCE, 'Freelance'),
        (INTERNSHIP, 'Internship')
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=30)
    employment_type = models.CharField(max_length=10, choices=EMPLOYMENT_TYPE_CHOICES, default=FULL_TIME)
    company_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    location_type = models.CharField(max_length=10, choices=LOCATION_TYPE_CHOICES, default=ON_SITE)
    start_date = models.DateField(auto_now_add=True)
    description = models.TextField()
    skills = models.TextField()
    media = models.FileField(blank=True, null=True)


class Education(TimeStampMixin):
    """Contain Education fields about the User."""

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='educations')
    school = models.CharField(max_length=40)
    degree = models.CharField(max_length=40)
    field_of_study = models.CharField(max_length=40)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=10)
    description = models.TextField()
    skills = models.TextField()
    media = models.FileField(blank=True, null=True)


class Certification(TimeStampMixin):
    """Contain Certifications fields about the User."""

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=40)
    issuing_organization = models.CharField(max_length=40)
    issue_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField(null=True, blank=True)
    credential_id = models.CharField(max_length=20, blank=True, null=True)
    credential_url = models.URLField()
    skills = models.TextField()


class Course(TimeStampMixin):
    """Contain Courses fields about the User."""

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courses')
    course_name = models.CharField(max_length=40)
    course_code = models.CharField(max_length=10)
    associated_with = models.CharField(max_length=40)
