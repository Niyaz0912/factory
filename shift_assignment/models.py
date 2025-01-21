from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse


class ShiftAssignment(models.Model):
    """
    Модель для хранения информации о заданиях операторов.

    Эта модель содержит данные о назначениях операторов на выполнение операций,
    включая информацию о станках, деталях и количестве.
    """

    operator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='assignments',
                                 null=True, blank=True,
                                 verbose_name="Оператор")
    master = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='master_assignments')
    operation_name = models.CharField(max_length=100, verbose_name="Операция")
    machine_id = models.CharField(max_length=50, verbose_name="№ станка")
    part_id = models.CharField(max_length=50, verbose_name="Наименование детали", default="")
    batch_number = models.CharField(max_length=50, verbose_name="Номер партии", default="")
    quantity = models.IntegerField(verbose_name="Количество")
    date = models.DateTimeField(default=timezone.now)  # Дата назначения задания
    file = models.FileField(upload_to='uploads/', blank=True, null=True)  # Файл, связанный с заданием

    def get_absolute_url(self):
        """
        Возвращает URL для доступа к деталям задания.

        Используется для генерации URL на основе первичного ключа задания.
        """
        return reverse('shift_assignment_detail', kwargs={'pk': self.pk})

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f'Задание: {self.operation_name}, Оператор: {self.operator}, Дата: {self.date}'

    class Meta:
        """Метаданные модели."""
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'


class CompletedShiftAssignment(models.Model):
    """
    Модель для хранения завершенных заданий операторов.

    Эта модель содержит данные о завершенных операциях,
    включая информацию о количестве брака и причинах остановки.
    """

    shift_assignment = models.ForeignKey(ShiftAssignment, on_delete=models.SET_NULL,
                                         related_name='completed_assignments', null=True)

    date = models.DateTimeField(default=timezone.now, verbose_name="Дата")  # Дата завершения задания
    operator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Оператор", on_delete=models.CASCADE)

    operation_name = models.CharField(max_length=255, verbose_name="Наименование операции")
    machine_id = models.CharField(max_length=50, verbose_name="№ станка")
    part_id = models.CharField(max_length=50, verbose_name="Наименование продукции")
    batch_number = models.CharField(max_length=50, verbose_name="№ партии")

    quantity = models.IntegerField(verbose_name="Количество")  # Общее количество выполненных операций
    defect_quantity = models.IntegerField(default=0, verbose_name="Количество брака")  # Количество бракованных изделий
    stop_reason = models.TextField(null=True, blank=True, verbose_name="Причина остановки станка")  # Причина остановки

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f'Завершенное задание: {self.operation_name}, Оператор: {self.operator}'

    class Meta:
        """Метаданные модели."""
        db_table = 'shift_assignment_completedshiftassignment'  # Указание имени таблицы в БД
        verbose_name = 'Завершенное задание'
        verbose_name_plural = 'Завершенные задания'


