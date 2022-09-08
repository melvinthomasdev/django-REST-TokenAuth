from django.contrib.auth.models import AbstractUser, BaseUserManager  # A new class is imported. ##
from django.db import models

from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist

YEAR_OF_STUDY_CHOICES = (
    ("1", "1st Year"),
    ("2", "2nd Year"),
    ("3", "3rd Year"),
    ("4", "4th Year"),
)


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    has_profile = models.BooleanField(default=False, blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_profile(self):
        try:
            profile = Profile.objects.get(user=self)
            return profile
        except ObjectDoesNotExist:
            return None


class Profile(models.Model):
    user = models.ForeignKey(to=User, related_name='profile', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=65, blank=False, null=False)
    contact = models.CharField(max_length=13, blank=False, null=False)
    college_name = models.CharField(max_length=150, blank=False, null=False)
    year_of_study = models.CharField(max_length=1, choices=YEAR_OF_STUDY_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.full_name
