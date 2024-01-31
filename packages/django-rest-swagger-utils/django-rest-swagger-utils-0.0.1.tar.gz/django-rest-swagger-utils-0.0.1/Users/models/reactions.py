from django.db import models

from Users.constants.enums import ReactionType
from Users.models.comment import Comment
from Users.models.post import Post
from Users.models.user_details import User


class Reaction(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,
                                default=None, null=True,
                                related_name='reactions')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None,
                             null=True, related_name='reactions')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='reactions')
    Reaction_Choice = (
        (ReactionType.LIKE.value, ReactionType.LIKE.value),
        (ReactionType.WOW.value, ReactionType.WOW.value),
        (ReactionType.HAHA.value, ReactionType.HAHA.value),
        (ReactionType.DISLIKE.value, ReactionType.DISLIKE.value),
        (ReactionType.SAD.value, ReactionType.SAD.value),
        (ReactionType.ANGRY.value, ReactionType.ANGRY.value)
    )
    reaction_type = models.CharField(max_length=10, choices=Reaction_Choice,
                                     default=None, null=True)

    def __str__(self):
        return self.reaction_type