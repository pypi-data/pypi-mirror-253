from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    profile_pic_url = models.CharField(max_length=2056, blank=True, null=True)
    password = models.CharField(max_length=24)
    short_description = models.CharField(max_length=256, blank=True, null=True)
    job_role = models.CharField(max_length=32,  blank=True, null=True)
    user_role = models.CharField(max_length=32, blank=True, null=True)
    first_name = models.CharField(max_length=64,  blank=True, null=True)
    last_name = models.CharField(max_length=32,  blank=True, null=True)
    
    groups = models.ManyToManyField(Group, verbose_name='Groups', blank=True, related_name='custom_user_set')

    # Define a unique related_name for the user_permissions relationship
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='User permissions',
        blank=True,
        related_name='custom_user_set'
    )

    def __int__(self):
        return self.username