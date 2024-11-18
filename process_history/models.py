from django.db import models
from django.conf import settings


class ProcessHistory(models.Model):
    process_name = models.CharField(max_length=255, default="Наименование операции:")
    detail_name = models.CharField(max_length=100, verbose_name="Наименование изделия")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    machine_id = models.IntegerField(default=1, verbose_name="ID станка")
    parameter_name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    detail_quantity = models.IntegerField(default=0, verbose_name="Количество деталей")
    assignment = models.ForeignKey('shift_assignment.ShiftAssignment', on_delete=models.SET_NULL, null=True, blank=True,
                                   verbose_name='Cменное задание')
    is_complete = models.BooleanField(default=False, verbose_name="Отметка о выполнении задания")

    def __str__(self):
        return f"{self.process_name} - {self.user} ({self.timestamp})"

    class Meta:
        verbose_name = 'process_history'
        verbose_name_plural = 'process_histories'
