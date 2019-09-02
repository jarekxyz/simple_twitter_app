from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.utils import timezone
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Tweet(models.Model):
    """Tweet object"""
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=255)
    tag = models.CharField(max_length=50)

    def __str__(self):
        return "{0}, {1}\n{2}\n{3}\n".format(self.author,
                                             self.date_created,
                                             self.text,
                                             self.tag)
