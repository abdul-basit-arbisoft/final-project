from rest_framework import serializers

from core.serializers import UserProfileSerializer
from .models import (
    Post, PostMedia, ReactionType, PostReaction, Comment,
    CommentReaction, CommentReply, ReplyReaction, HashTag 
)


class PostMediaSerializer(serializers.ModelSerializer):
    """Serializer class for Post media"""

    class Meta:
        model = PostMedia
        fields = '__all__'


class ReactionTypeSerializer(serializers.ModelSerializer):
    """Serializer class for reaction types."""

    class Meta:
        model = ReactionType
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Serializer class for posts."""

    post_owner = UserProfileSerializer()
    post_images = PostMediaSerializer(many=True)
    reacted_by = serializers.StringRelatedField(many=True)
    commented_by = serializers.StringRelatedField(many=True)
    viewed_by = UserProfileSerializer(many=True)
    shared_by = UserProfileSerializer(many=True)
    text_body = serializers.CharField()
    number_of_reactions = serializers.SerializerMethodField()
    number_of_comments = serializers.SerializerMethodField()
    time_difference = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
    
    def get_number_of_reactions(self, obj):
        """Number of reactions on post."""
        return obj.number_of_reactions

    def get_number_of_comments(self, obj):
        """Number of comments on a post."""
        return obj.number_of_comments

    def get_time_difference(self, obj):
        """How long ago the post was uploaded."""
        return obj.time_difference


class PostReactionSerializer(serializers.ModelSerializer):
    """Serializer class for post reactions."""

    class Meta:
        model = PostReaction
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Serializer class for comments"""

    post = PostSerializer()
    comment_owner = UserProfileSerializer()
    reacted_by = serializers.StringRelatedField(many=True)
    replied_by = serializers.StringRelatedField(many=True)

    class Meta:
        model = Comment
        fields = '__all__'


class CommentReactionSerializer(serializers.ModelSerializer):
    """Serializer class for Comments reactions."""

    comment = CommentSerializer()
    reaction_owner = UserProfileSerializer()

    class Meta:
        model = CommentReaction
        fields = '__all__'


class CommentReplySerializer(serializers.ModelSerializer):
    """Serializer class for Comment replies"""

    comment = CommentSerializer()
    reply_owner = UserProfileSerializer()
    reacted_by = serializers.StringRelatedField(many=True)

    class Meta:
        model = CommentReply
        fields = '__all__'


class ReplyReactionSerializer(serializers.ModelSerializer):
    """Serializer class for replies reactions"""

    comment_reply = CommentReplySerializer()
    reaction_owner = UserProfileSerializer()

    class Meta:
        model = ReplyReaction
        fields = '__all__'


class HashTagSerializer(serializers.ModelSerializer):
    """Serializer class for hashtags."""

    associated_posts = PostSerializer(many=True)
    followed_by = UserProfileSerializer(many=True)

    class Meta:
        model = HashTag
        fields = '__all__'
