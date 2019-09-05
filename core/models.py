from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.user_type = 'Admin'
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, default='')
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    user_type = models.CharField(max_length=255, default='Customer')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    region = models.ForeignKey(
        'Region',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Suburb(models.Model):
    city = models.ForeignKey(
        'City',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Property(models.Model):
    """Property Object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/property')
    region = models.ForeignKey(
        'Region',
        on_delete=models.SET_NULL,
        null=True
    )
    city = models.ForeignKey(
        'City',
        on_delete=models.SET_NULL,
        null=True
    )
    suburb = models.ForeignKey(
        'Suburb',
        on_delete=models.SET_NULL,
        null=True
    )
    address = models.CharField(max_length=255, default='')
    propertyType = models.CharField(max_length=40)
    rooms = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Property)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)
