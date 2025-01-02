from django.contrib import admin
from .models import ShiftAssignment, CompletedShiftAssignment


class ShiftAssignmentAdmin(admin.ModelAdmin):
    list_display = ('operation_name', 'operator', 'machine_id', 'part_id', 'batch_number', 'quantity')
    search_fields = ('operation_name', 'operator__username', 'machine_id', 'part_id', 'batch_number')
    list_filter = ('operator', 'machine_id')


admin.site.register(ShiftAssignment, ShiftAssignmentAdmin)


class CompletedShiftAssignmentAdmin(admin.ModelAdmin):
    list_display = (
        'operation_name', 'operator', 'machine_id', 'part_id', 'batch_number', 'quantity', 'defect_quantity',
        'stop_reason',
        'shift_assignment')
    list_filter = ('operator', 'machine_id', 'shift_assignment')
    search_fields = ('operation_name', 'part_id', 'batch_number')
    ordering = ('-id',)  # Сортировка по убыванию ID


# Регистрация модели с классом админки
admin.site.register(CompletedShiftAssignment, CompletedShiftAssignmentAdmin)
