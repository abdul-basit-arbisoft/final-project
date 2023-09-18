from django.contrib import admin

from .models import (
    Post, PostMedia, ReactionType, PostReaction, Comment,
    CommentReaction, CommentReply, ReplyReaction, HashTag 
)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Addresses admin for Post Model."""

    list_display = ('id', 'post_owner', 'parent_post', 'text_body', 'edited')

@admin.register(PostMedia)
class PostMediaAdmin(admin.ModelAdmin):
    """Addresses admin for PostMedia Model."""

    list_display = ('id', 'post', 'image', 'created_at')

@admin.register(ReactionType)
class ReactionTypeAdmin(admin.ModelAdmin):
    """Addresses admin for Reaction type model."""

    list_display = ('id', 'type', 'created_at')

@admin.register(PostReaction)
class PostReactionAdmin(admin.ModelAdmin):
    """Addresses admin for Post reactions Model."""

    list_display = ('id', 'post', 'reaction_by', 'reaction_type', 'created_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Addresses admin for Comments Model."""

    list_display = ('id', 'post', 'comment_owner', 'text', 'created_at')

@admin.register(CommentReaction)
class CommentReactionAdmin(admin.ModelAdmin):
    """Addresses admin for Comments reactions Model."""

    list_display = ('id', 'comment', 'reaction_owner', 'reaction_type', 'created_at')

@admin.register(CommentReply)
class CommentReplyAdmin(admin.ModelAdmin):
    """Addresses admin for Comments reply Model."""

    list_display = ('id', 'comment', 'reply_owner', 'text', 'created_at')

@admin.register(ReplyReaction)
class ReplyReactionAdmin(admin.ModelAdmin):
    """Addresses admin for reply reaction Model."""

    list_display = ('id', 'comment_reply', 'reaction_owner', 'reaction_type', 'created_at')

@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    """Addresses admin for hashtag Model."""

    list_display = ('id', 'topic', 'created_at')
