from django.db import models
from Users.models.user_details import User
from Users.models.domains import Domain


class DomainExpert(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    domain = models.ForeignKey(Domain, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)