from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home_view'),

    path('register/', views.UserRegistrationView.as_view(), name='register'),

    path('login/',  TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('change_password/<int:pk>/', views.ChangePasswordView.as_view(), name='change_password'),
    path('update_profile/<int:pk>/', views.UpdateUserProfileView.as_view(), name='Update_profile'),

    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('logout_all/', views.LogoutAllView.as_view(), name='logout_all'),

    path('user_profiles/', views.UserProfileListCreateView.as_view(), name='user_profile_list'),
    path('user_profiles/<int:pk>/', views.UserProfileDetailView.as_view(), name='user_profile_detail'),

    path('experiences/', views.ExperienceListCreateView.as_view(), name='experience_list'),
    path('experiences/<int:pk>/', views.ExperienceDetailView.as_view(), name='experience_detail'),

    path('educations/', views.EducationListCreateView.as_view(), name='education_list'),
    path('educations/<int:pk>/', views.EducationDetailView.as_view(), name='education_detail'),

    path('certifications/', views.CertificationListCreateView.as_view(), name='certification_list'),
    path('certifications/<int:pk>/', views.CertificationDetailView.as_view(), name='certification_detail'),

    path('courses/', views.CourseListCreateView.as_view(), name='course_list'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
]
