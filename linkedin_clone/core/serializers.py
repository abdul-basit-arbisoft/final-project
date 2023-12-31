from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from .models import UserProfile, Experience, Education, Certification, Course, Follow

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializer to register new user to the app."""

    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        """To validate the password."""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        """To create new user data, in the database."""
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    """Serializer class to change user password."""

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        """To validate the new password."""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        """To validate the old password."""
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        """To update user data, in the database."""
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class UpdateUserSerializer(serializers.ModelSerializer):
    """Serializer to update username, first_name, last_name and password."""

    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'username': {'required': True},
        }

    def validate_email(self, value):
        """To validate user email, So it should be unique."""

        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        """To validate user username, So it should be unique."""

        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        """To update user data, in the database."""

        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']

        instance.save()

        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer class for the user."""

    followers_count =serializers.SerializerMethodField()
    following_count =serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = (
            'id', 'user', 'profile_pic', 'cover_pic', 'headline', 'summary',
            'location', 'industry', 'website', 'phone_number', 'birthdate',
            'age', 'gender', 'followers_count', 'following_count'
        )

    def get_followers_count(self, obj):
        """Number of followers for this UserProfile."""
        return obj.following.count()

    def get_following_count(self, obj):
        """Number of people this UserProfile is following."""
        return obj.followers.count()


class FollowersSerializer(serializers.ModelSerializer):
    """Serializer class for Follow model"""

    class Meta:
        model = Follow
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    """Serializer class for Experiences of user."""

    class Meta:
        model = Experience
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    """Serializer class for Education of user."""

    class Meta:
        model = Education
        fields = '__all__'


class CertificationSerializer(serializers.ModelSerializer):
    """Serializer class for Certifications of user."""

    class Meta:
        model = Certification
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    """Serializer class for Courses of user."""

    class Meta:
        model = Course
        fields = '__all__'
