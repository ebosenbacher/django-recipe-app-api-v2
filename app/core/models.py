"""
Database models.
"""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""

        if not email:
            raise ValueError('User must have an email address')

        normalized_email = self.normalize_email(email=email)
        # create user
        user = self.model(
            email=normalized_email,
            **extra_fields)

        # set the password in a secure way
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""

        superuser = self.create_user(
            email=email,
            password=password
        )
        # allows login to the admin panel
        superuser.is_staff = True
        # allows to perform all operations in the admin panel
        superuser.is_superuser = True
        superuser.save(using=self._db)

        return superuser


class user(AbstractBaseUser, PermissionsMixin):
    """User in the system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # custom model manager
    objects = UserManager()

    USERNAME_FIELD = 'email'


class Recipe(models.Model):
    """Recipe object."""

    user = models.ForeignKey(
          settings.AUTH_USER_MODEL,
          on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.title
