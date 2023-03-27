from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models



class UserManager(BaseUserManager):
    def _create_user(self, username, password, **kwargs):
        username = username
        is_staff = kwargs.pop("is_staff", False)
        is_superuser = kwargs.pop("is_superuser", False)
        is_active = kwargs.pop("is_active", True)

        user = self.model(
            username=username,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            password=password,
            **kwargs
        )
        user.save(using=self._db)


        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(
            username,
            password,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_readonly = models.BooleanField(default=False)
    username = models.CharField(null=False, max_length=125,unique=True)
    password = models.CharField(null=False, max_length=255)
    author_pseudonym= models.CharField(null=False, max_length=255)
    remember_created_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)
    

    class Meta:
        indexes = [
            models.Index(fields=["username"]),
            
        ]
        app_label = "acc"
        db_table = "User"

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username
