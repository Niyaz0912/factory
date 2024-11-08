from django.db import models

from django.conf import settings


class ProcessHistory(models.Model):
    detail_name = models.CharField(max_length=100, verbose_name="Наименование изделия")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL)
    parameter_name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    detail_quantity = models.IntegerField(default=0, verbose_name="Количество деталей")

    def __str__(self):
        return f'{self.detail_name}, {self.user}'

    class Meta:
        verbose_name = 'process history'
        verbose_name_plural = 'process histories'
