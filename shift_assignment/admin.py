from django.contrib import admin
from .models import ShiftAssignment


class ShiftAssignmentAdmin(admin.ModelAdmin):
    list_display = ('operation_name', 'operator', 'machine_id', 'part_id', 'batch_number', 'quantity')
    search_fields = ('operation_name', 'operator__username', 'machine_id', 'part_id', 'batch_number')
    list_filter = ('operator', 'machine_id')


admin.site.register(ShiftAssignment, ShiftAssignmentAdmin)
