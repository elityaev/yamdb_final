from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_username

ROLES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Администратор'),
)


class UserRole:
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=(validate_username,)
    )
    email = models.EmailField(max_length=254, unique=True, blank=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    role = models.CharField(
        verbose_name='роль',
        choices=ROLES,
        max_length=20,
        default=UserRole.USER,
    )
    bio = models.TextField(verbose_name='биография', blank=True)
    confirmation_code = models.CharField(
        max_length=30,
        null=True,
        default='XXXX'
    )

    @property
    def is_user(self):
        return self.role == UserRole.USER

    @property
    def is_admin(self):
        return self.role == UserRole.ADMIN

    @property
    def is_moderator(self):
        return self.role == UserRole.MODERATOR

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.username
