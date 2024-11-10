from django.db import models
from django.conf import settings
from users.models import User


class ProcessHistory(models.Model):
    process_name = models.CharField(max_length=255, default="Процесс ...")
    detail_name = models.CharField(max_length=100, verbose_name="Наименование изделия")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    machine_id = models.IntegerField(default=1, verbose_name="ID станка")
    parameter_name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    detail_quantity = models.IntegerField(default=0, verbose_name="Количество деталей")

    def __str__(self):
        return f"{self.process_name} - {self.user} ({self.timestamp})"

    class Meta:
        verbose_name = 'process history'
        verbose_name_plural = 'process histories'


class ShiftAssignment(models.Model):
    operator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Оператор")
    operation_name = models.CharField(max_length=100, default="Не указано", verbose_name="Операция")
    machine_id = models.CharField(max_length=50, verbose_name="№ станка")
    part_id = models.CharField(max_length=50, verbose_name="Наименование детали")
    batch_number = models.CharField(max_length=50, verbose_name="Номер партии")
    quantity = models.IntegerField(verbose_name="Количество")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")

    def __str__(self):
        return f'Задание: {self.batch_number}, Оператор: {self.operator}, Дата: {self.date}'

    class Meta:
        verbose_name = 'Сменное задание'
        verbose_name_plural = 'Сменные задания'
