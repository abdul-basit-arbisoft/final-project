from django.db import models
from core.models import UserProfile
from django.utils import timezone

from core.models import TimeStampMixin


class Post(TimeStampMixin):
    """User Post."""

    post_owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='posts')
    parent_post = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    text_body = models.TextField(max_length=500)
    saved_by = models.ManyToManyField(UserProfile, related_name='saves_posts', blank=True)
    edited = models.BooleanField(default=False)
    shared_by = models.ManyToManyField(UserProfile, related_name='shared_posts', blank=True)
    reacted_by = models.ManyToManyField(UserProfile, through='PostReaction', related_name='reacted_posts', blank=True)
    commented_by = models.ManyToManyField(UserProfile, through='Comment', related_name='commented_posts', blank=True)
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.post_owner.user.username} --> Post{self.id}"

    @property
    def number_of_reactions(self):
        """Number of reactions on post."""
        if self.reacted_by.count() == 1:
            return f"{self.reacted_by.count()} like"

        return f"{self.reacted_by.count()} likes"
    
    @property
    def number_of_comments(self):
        """Number of comments on a post"""
        comments = Comment.objects.filter(post=self).count()
        if comments == 0:
            return ""
        elif comments == 1:
            return f"View {comments} comment"
        return f"View all {comments} comments"
    
    @property
    def time_difference(self):
        """How long the post was uploaded."""
        time_difference = timezone.now() - self.created_at
        total_seconds = time_difference.seconds
        hour = total_seconds // (60 * 60)
        minute = (total_seconds - hour * 60 * 60) // 60
        seconds = total_seconds- (hour * 60  * 60) - (minute * 60)

        if(time_difference.days):
            return f"{time_difference.days} days ago"

        if(hour != 0):
            if(hour == 1):
                return f"{minute} hour ago"
            return f"{hour} hours ago"
        elif(minute != 0):
            if(minute == 1):
                return f"{minute} minute ago"
            return f"{minute} minutes ago"
        else:
            return f"{seconds} seconds ago"


class PostMedia(TimeStampMixin):
    """Images of a post."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_images')
    image = models.ImageField(upload_to='Posts/Images/')


    class Meta:
        verbose_name = 'Post Image'
        verbose_name_plural = 'Post Images'


class ReactionType(TimeStampMixin):
    """Reaction Types on a post."""

    LIKE = "like"
    CELEBRATE = "celebrate"
    SUPPORT = "support"
    LOVE = "love"
    INSIGHTFUL = "insightful"
    FUNNY = "funny"
    
    REACTION_TYPE_CHOICES = [
        (LIKE, "Like"),
        (CELEBRATE, "Celebrate"),
        (SUPPORT, "Support"),
        (LOVE, "Love"),
        (FUNNY, "Funny"),
        (INSIGHTFUL, "Insightful"),
    ]

    type = models.CharField(max_length=12, choices=REACTION_TYPE_CHOICES, default=None)

    class Meta:
        verbose_name = 'Reaction Type'
        verbose_name_plural = 'Reaction Types'

    def __str__(self):
        return f"{self.type}"


class PostReaction(TimeStampMixin):
    """reactions on a post."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reaction_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='post_reactions')
    reaction_type = models.ForeignKey(ReactionType, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.reaction_by.user.username} --> {self.reaction_type} --> {self.post}"


class Comment(TimeStampMixin):
    """Comments on a post."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    reacted_by = models.ManyToManyField(UserProfile, through='CommentReaction', related_name="reacted_comments")
    replied_by = models.ManyToManyField(UserProfile, through='CommentReply',related_name = "replied_comments")

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return f"Comment by --> {self.comment_owner.user.username}"
    
    @property
    def time_difference(self):
        """How long the post was uploaded."""
        time_difference = timezone.now() - self.created_at
        total_seconds = time_difference.seconds
        hour = total_seconds // (60 * 60)
        minute = (total_seconds - hour * 60 * 60) // 60
        seconds = total_seconds- (hour * 60  * 60) - (minute * 60)

        if(time_difference.days):
            return f"{time_difference.days} days ago"

        if(hour != 0):
            if(hour == 1):
                return f"{minute} hour ago"
            return f"{hour} hours ago"
        elif(minute != 0):
            if(minute == 1):
                return f"{minute} minute ago"
            return f"{minute} minutes ago"
        else:
            return f"{seconds} seconds ago"


class CommentReaction(TimeStampMixin):
    """Reactions on user comment."""

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reaction_owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    reaction_type = models.ForeignKey(ReactionType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Comment Reaction'
        verbose_name_plural = 'Comment Reactions'
        unique_together = (('comment', 'reaction_owner'))


class CommentReply(TimeStampMixin):
    """Reply to a user comment"""

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply_owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    reacted_by = models.ManyToManyField(UserProfile, through='ReplyReaction', related_name="reacted_replies")

    class Meta:
        verbose_name = 'Comment Reply'
        verbose_name_plural = 'Comment Replies'


class ReplyReaction(TimeStampMixin):
    """Reply reaction to a comment."""
    
    comment_reply = models.ForeignKey(CommentReply, on_delete=models.CASCADE)
    reaction_owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    reaction_type = models.ForeignKey(ReactionType, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Reply Reaction'
        verbose_name_plural = 'Reply Reactions'
        unique_together = (('comment_reply', 'reaction_owner'))


class HashTag(TimeStampMixin):
    """Hashtags on posts."""

    topic = models.CharField(max_length=100)
    associated_posts = models.ManyToManyField(Post, related_name='hashtags', blank=True)
    followed_by = models.ManyToManyField(UserProfile, related_name='followed_hashtags')

    class Meta:
        verbose_name = 'Hashtag'
        verbose_name_plural = 'Hashtags'
