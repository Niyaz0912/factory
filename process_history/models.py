from django.db import models
from django.conf import settings
from django.urls import reverse


class ProcessHistory(models.Model):
    CONTROL_CODE_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('3;2', '3;2'),  # Допустимый код с разделителем
    ]

    process_name = models.CharField(max_length=255, verbose_name="Наименование операции:")
    detail_name = models.CharField(max_length=100, verbose_name="Наименование изделия")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name="Оператор")
    machine_id = models.IntegerField(default=1, verbose_name="№ станка")
    parameter_name = models.CharField(max_length=100, verbose_name="Параметры")
    value = models.CharField(max_length=100, verbose_name="Значение специальной характеристики")
    timestamp = models.DateTimeField(auto_now_add=True)
    detail_quantity = models.IntegerField(default=0, verbose_name="Количество деталей")
    assignment = models.ForeignKey('shift_assignment.ShiftAssignment', on_delete=models.SET_NULL, null=True, blank=True,
                                   verbose_name='Сменное задание')
    mark_yes_no = models.BooleanField(default=True, verbose_name="Отметка да/нет")

    # Поле для кода контроля
    control_code = models.CharField(max_length=10, choices=CONTROL_CODE_CHOICES, default=1, verbose_name="Код контроля")

    # Новые поля для параметров контроля
    roughness_check = models.CharField(max_length=1, choices=[('+', '+'), ('-', '-')], default='+', verbose_name="Шероховатость")
    defects_check = models.CharField(max_length=1, choices=[('+', '+'), ('-', '-')],
                                     default='+', verbose_name="Отсутствие рисок, канавок и т.д.")

    threading_check = models.CharField(max_length=1, choices=[('+', '+'), ('-', '-')],
                                       default='+', verbose_name="Наличие резьбы и отверстия под шплинт")
    diameter_check = models.CharField(max_length=1, choices=[('+', '+'), ('-', '-')],
                                      default='+', verbose_name="Диаметр галтели")
    is_complete = models.BooleanField(default=False, verbose_name="Завершено")

    def get_absolute_url(self):
        return reverse('process_history_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.process_name} - {self.user} ({self.timestamp})"

    class Meta:
        verbose_name = 'process_history'
        verbose_name_plural = 'process_histories'
