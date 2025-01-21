from django.contrib import admin
from .models import ShiftAssignment, CompletedShiftAssignment


class ShiftAssignmentAdmin(admin.ModelAdmin):
    """
    Административный интерфейс для модели ShiftAssignment.

    Этот класс определяет, какие поля будут отображаться в списке
    объектов модели ShiftAssignment в административной панели,
    а также предоставляет возможность поиска и фильтрации.
    """

    # Поля, которые будут отображаться в списке объектов
    list_display = ('operation_name', 'operator', 'machine_id', 'part_id', 'batch_number', 'quantity')

    # Поля, по которым можно осуществлять поиск
    search_fields = ('operation_name', 'operator__username', 'machine_id', 'part_id', 'batch_number')

    # Поля для фильтрации списка объектов
    list_filter = ('operator', 'machine_id')


# Регистрация модели ShiftAssignment с использованием кастомного администратора
admin.site.register(ShiftAssignment, ShiftAssignmentAdmin)


class CompletedShiftAssignmentAdmin(admin.ModelAdmin):
    """
    Административный интерфейс для модели CompletedShiftAssignment.

    Этот класс определяет, какие поля будут отображаться в списке
    объектов модели CompletedShiftAssignment в административной панели,
    а также предоставляет возможность поиска и фильтрации.
    """

    # Поля, которые будут отображаться в списке объектов
    list_display = (
        'operation_name', 'operator', 'machine_id', 'part_id', 'batch_number',
        'quantity', 'defect_quantity', 'stop_reason', 'shift_assignment'
    )

    # Поля для фильтрации списка объектов
    list_filter = ('operator', 'machine_id', 'shift_assignment')

    # Поля, по которым можно осуществлять поиск
    search_fields = ('operation_name', 'part_id', 'batch_number')

    # Сортировка по убыванию ID
    ordering = ('-id',)


# Регистрация модели CompletedShiftAssignment с использованием кастомного администратора
admin.site.register(CompletedShiftAssignment, CompletedShiftAssignmentAdmin)
