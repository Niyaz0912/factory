from django.db import models
from django.urls import reverse
from django.utils import timezone

from users.models import User


class ShiftAssignment(models.Model):
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='operator', null=True, blank=True,
                                 verbose_name="Оператор")
    operation_name = models.CharField(max_length=100, verbose_name="Операция")
    machine_id = models.CharField(max_length=50, verbose_name="№ станка")
    part_id = models.CharField(max_length=50, verbose_name="Наименование детали")
    batch_number = models.CharField(max_length=50, verbose_name="Номер партии")
    quantity = models.IntegerField(verbose_name="Количество")
    date = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('shift_assignment_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Задание: {self.operation_name}, Оператор: {self.operator}, Дата: {self.date}'

    class Meta:
        verbose_name = 'shift_assignment'
        verbose_name_plural = 'shift_assignment'
