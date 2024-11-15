from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    OPERATOR = 'operator', _('Operator')
    MASTER = 'master', _('Master')
    ADMIN = 'admin', _('Administrator')


class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, blank=False, null=False, default='имя оператора', verbose_name="имя сотрудника")
    last_name = models.CharField(max_length=30, blank=False, null=False, default='фамилия оператора', verbose_name="фамилия сотрудника")
    username = models.CharField(max_length=150, unique=True, blank=False, null=False)
    password = models.CharField(max_length=255, verbose_name="пароль")
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.OPERATOR, verbose_name="должность")  # Роль пользователя
    is_active = models.BooleanField(default=True, verbose_name='active', **NULLABLE)

    USERNAME_FIELD = "username"  # Используем username для авторизации
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']  # Обязательные поля

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']