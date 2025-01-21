from django.contrib import admin
from .models import ProcessHistory


class ProcessHistoryAdmin(admin.ModelAdmin):
    """
    Административный интерфейс для модели ProcessHistory.

    Этот класс определяет, какие поля будут отображаться в списке
    объектов модели ProcessHistory в административной панели.
    """

    # Определение полей, которые будут отображаться в списке объектов
    list_display = ('user', 'machine_id', 'part_id', 'batch_number', 'timestamp')


# Регистрация модели ProcessHistory с использованием кастомного администратора
admin.site.register(ProcessHistory, ProcessHistoryAdmin)

