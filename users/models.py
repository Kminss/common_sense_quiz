from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models
from users.managers import UserManager


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(default="", max_length=30, unique=True, null=False, blank=False)
    nickname = models.CharField(default="", max_length=30, unique=True, null=False, blank=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, perm, obj=None):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        app_label = 'users'
        db_table = 'quiz_users'
