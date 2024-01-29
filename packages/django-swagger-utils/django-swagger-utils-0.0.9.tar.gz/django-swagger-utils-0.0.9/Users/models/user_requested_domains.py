from django.db import models
from gyaan.models.user_details import User
from gyaan.models.domains import Domain


class UserRequestedDomain(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    domain = models.ForeignKey(Domain, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)