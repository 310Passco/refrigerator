from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator




class Manager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(_('username'), unique=True, max_length=150, blank=False)
    email = models.EmailField(_('email address'), unique=True)

    objects = Manager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Food(models.Model):
    owner = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    deadline = models.DateField(null=True)
    quantity = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1,'最小値は1です'), MaxValueValidator(100,'最大値は100です')])
    #validatorsが機能していないが解決する時間がなくエラーはないので保留