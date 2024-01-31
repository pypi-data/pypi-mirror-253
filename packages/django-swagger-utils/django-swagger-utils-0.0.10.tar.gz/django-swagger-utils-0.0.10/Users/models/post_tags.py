from django.db import models
from Users.models.post import Post
from Users.models.domains import Domain


class DomainTag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.DO_NOTHING, default=None, null=False, blank=True)
    tag_name = models.CharField(max_length=32)
    domain_id = models.ForeignKey(Domain, on_delete=models.DO_NOTHING, default=None, null=False, blank=False)