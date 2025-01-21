from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Определение параметров для полей, которые могут быть пустыми
NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    """
    Определение ролей пользователей с использованием TextChoices.

    Это перечисление содержит доступные роли пользователей в системе:
    - Оператор
    - Мастер
    - Администратор
    """
    OPERATOR = 'operator', _('Operator')
    MASTER = 'master', _('Master')
    ADMIN = 'admin', _('Administrator')


class User(AbstractUser):
    """
    Модель пользователя, расширяющая стандартную модель AbstractUser.

    Эта модель добавляет дополнительные поля и функциональность для пользователей системы.
    """

    is_staff = models.BooleanField(default=False)  # Указывает, является ли пользователь сотрудником
    first_name = models.CharField(max_length=30, blank=False, null=False, default='имя оператора',
                                  verbose_name="имя сотрудника")
    last_name = models.CharField(max_length=30, blank=False, null=False, default='фамилия оператора',
                                 verbose_name="фамилия сотрудника")

    username = models.CharField(max_length=150, unique=True, blank=False, null=False)  # Уникальное имя пользователя
    password = models.CharField(max_length=255, verbose_name="пароль")  # Пароль пользователя

    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.OPERATOR,
                            verbose_name="должность")  # Роль пользователя
    is_active = models.BooleanField(default=True, verbose_name='active',
                                    **NULLABLE)  # Указывает, активен ли пользователь

    USERNAME_FIELD = "username"  # Поле для аутентификации
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Обязательные поля при создании пользователя

    def __str__(self):
        """Возвращает строковое представление объекта пользователя."""
        return f'{self.first_name} {self.last_name}'

    class Meta:
        """Метаданные модели."""
        verbose_name = 'User'  # Человекочитаемое имя в единственном числе
        verbose_name_plural = 'Users'  # Человекочитаемое имя во множественном числе
        ordering = ['id']  # Сортировка по ID по умолчанию


