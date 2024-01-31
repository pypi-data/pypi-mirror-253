from django.db import models

from Users.models.domains import Domain
from Users.models.user_details import User


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=526)
    post_content = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None, blank=True)
    posted_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    domain = models.ForeignKey(Domain, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)

    class Meta:
        get_latest_by = 'posted_at'