from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken, BlacklistedToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model

from .serializers import (
    RegistrationSerializer, ChangePasswordSerializer, UpdateUserSerializer, UserProfileSerializer,
    EducationSerializer, ExperienceSerializer, CourseSerializer, CertificationSerializer, FollowersSerializer
)
from .models import UserProfile, Education, Certification, Course, Experience

User = get_user_model()


class UserRegistrationView(generics.CreateAPIView):
    """View to register new user."""

    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


class ChangePasswordView(generics.UpdateAPIView):
    """View to Change old password."""

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer


class UpdateUserProfileView(generics.UpdateAPIView):
    """View to Update User Profile."""

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateUserSerializer


class LogoutView(APIView):
    """To Logout user from a device."""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
 

class LogoutAllView(APIView):
    """To Logout user from all devices."""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            _, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)


class UserProfileListCreateView(generics.ListCreateAPIView):
    """Handles the listing and creation of user profiles."""

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        """Returns only the object related to current user"""
        user = self.request.user
        return UserProfile.objects.filter(user=user)




class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Handles the retrieval, updating, and deletion of individual user profiles."""

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]



class EducationListCreateView(generics.ListCreateAPIView):
    """Handles the listing and creation of user's Education."""

    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]


class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Handles the retrieval, updating, and deletion of individual user's Education."""

    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]


class CertificationListCreateView(generics.ListCreateAPIView):
    """Handles the listing and creation of user's Certifications."""

    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = [IsAuthenticated]


class CertificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Handles the retrieval, updating, and deletion of individual user's Certification."""

    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = [IsAuthenticated]


class ExperienceListCreateView(generics.ListCreateAPIView):
    """Handles the listing and creation of user's Experience."""

    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]


class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Handles the retrieval, updating, and deletion of individual user's Experience."""

    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]


class CourseListCreateView(generics.ListCreateAPIView):
    """Handles the listing and creation of user's Course."""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Handles the retrieval, updating, and deletion of individual user's Course."""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


def home_view(request):
    """To display the home page."""

    return render(request, 'core/base.html')