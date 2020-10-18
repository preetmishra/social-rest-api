from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for UserProfile."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile."""

        if not email:
            raise ValueError('Please specify an e-mail address.')
        email = self.normalize_email(email) # Normalize the domain part.

        # Create a new instance of UserProfile.
        user = self.model(email=email, name=name)
        user.set_password(password)

        user.save(using=self._db)  # Use the default database.
        return user

    def create_superuser(self, email, name, password):
        """Creates a new superuser."""

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Custom Manager.
    objects = UserProfileManager()

    # Use the email field for user authentication.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Returns user's full name."""

        return self.name

    def get_short_name(self):
        """Returns user's short name."""

        return self.name

    def __str__(self):
        """String representation for UserProfile instance."""

        return self.email


class ProfileFeedItem(models.Model):
    """Database model for profile feed items."""

    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation for ProfileFeedItem instance."""

        return self.status_text
