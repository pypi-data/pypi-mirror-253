from django.db import models
from Users.models.user_details import User
from Users.models.post import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, default=None, blank=False, null=False)
    comment_id = models.AutoField(primary_key=True)
    comment_text = models.TextField()
    commented_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, blank=False, null=False)
    is_answer = models.BooleanField(default=False)
    reply = models.ForeignKey('self', on_delete=models.DO_NOTHING, default=None, blank=True, null=True)