from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        # Normalize email address
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # Set password
        user.set_password(password)

        # Save user model
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create a new superuser profile"""
        user = self.create_user(email, name, password)

        # Set superuser status
        user.is_superuser = True
        user.is_staff = True

        # Save user model
        user.save(using=self._db)

        return user


def create_user(self, email, name, password=None):
    """Create a new user profile"""
    if not email:
        raise ValueError('Users must have an email address')

    # Normalize email address
    email = self.normalize_email(email)
    user = self.model(email=email, name=name)

    # Set password
    user.set_password(password)

    # Save user model
    user.save(using=self._db)

    return user


def create_superuser(self, email, name, password):
    """Create a new superuser profile"""
    user = self.create_user(email, name, password)

    # Set superuser status
    user.is_superuser = True
    user.is_staff = True

    # Save user model
    user.save(using=self._db)

    return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)  # max_length is required
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)  # default is optional
    is_staff = models.BooleanField(default=False)

    # Override the default username field with email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # Create a model manager
    objects = UserProfileManager()

    # Django uses this to convert objects to strings
    def __str__(self):
        """Return string representation of our user"""
        return self.email

    # Add custom functions to our model
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
