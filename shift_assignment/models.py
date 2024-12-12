from django.db import models
from django.conf import settings
from django.utils import timezone


class ShiftAssignment(models.Model):
    batch_number = models.CharField(max_length=100)  # Пример поля
    operation_name = models.CharField(max_length=100)  # Пример поля
    quantity = models.IntegerField()  # Пример поля
    operator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)  # Обновлено
    part_id = models.CharField(max_length=50)  # Пример поля
    machine_id = models.IntegerField()  # Пример поля
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.operation_name} - {self.batch_number}'

    class Meta:
        verbose_name = 'shift_assignment'
        verbose_name_plural = 'shift_assignment'
