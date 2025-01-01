from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse


class ShiftAssignment(models.Model):
    operator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='assignments', null=True, blank=True,
                                 verbose_name="Оператор")
    master = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='master_assignments')
    operation_name = models.CharField(max_length=100, verbose_name="Операция")
    machine_id = models.CharField(max_length=50, verbose_name="№ станка")
    part_id = models.CharField(max_length=50, verbose_name="Наименование детали", default="")
    batch_number = models.CharField(max_length=50, verbose_name="Номер партии", default="")
    quantity = models.IntegerField(verbose_name="Количество")
    date = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('shift_assignment_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Задание: {self.operation_name}, Оператор: {self.operator}, Дата: {self.date}'

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'


class CompletedShiftAssignment(models.Model):
    shift_assignment = models.ForeignKey(ShiftAssignment, on_delete=models.CASCADE,
                                         related_name='completed_assignments')
    operator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Указывает на оператора
    operation_name = models.CharField(max_length=255)
    machine_id = models.CharField(max_length=50)
    part_id = models.CharField(max_length=50)
    batch_number = models.CharField(max_length=50)
    quantity = models.IntegerField()
    defect_quantity = models.IntegerField(default=0)
    stop_reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Завершенное задание: {self.operation_name}, Оператор: {self.operator}'

    class Meta:
        db_table = 'shift_assignment_completedshiftassignment'
        verbose_name = 'Завершенное задание'
        verbose_name_plural = 'Завершенные задания'


