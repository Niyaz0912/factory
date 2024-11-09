# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _
#
# NULLABLE = {'blank': True, 'null': True}
#
#
# class UserRoles(models.TextChoices):
#     ADMIN = 'admin', _('admin')
#     MASTER = 'master', _('master')
#     USER = 'user', _('user')
#
#
# class User(AbstractUser):
#     username = None
#     email = models.EmailField(unique=True, verbose_name='email')
#     role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.USER)
#     phone = models.CharField(max_length=35, verbose_name='telephone_number', **NULLABLE)
#     telegram = models.CharField(max_length=150, verbose_name='Telegram_username', **NULLABLE)
#     is_active = models.BooleanField(default=True, verbose_name='active')
#
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []
#
#     def __str__(self):
#         return f'{self.email}'
#
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'
#         ordering = ['id']
#
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    ADMIN = 'admin', _('admin')
    MASTER = 'master', _('master')
    USER = 'user', _('user')


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)  # Теперь поле допускает NULL  # Уникальное поле username
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.USER)
    phone = models.CharField(max_length=35, verbose_name='telephone_number', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='active')

    USERNAME_FIELD = "username"  # Используем username для авторизации
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Обязательные поля

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']