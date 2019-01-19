from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):

    def create_user(self, email, password, *args, **kwargs):
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
