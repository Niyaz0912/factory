from django.contrib import admin
from process_history.models import ProcessHistory


@admin.register(ProcessHistory)
class ProcessHistory(admin.ModelAdmin):
    list_display = ('process_name', 'detail_name', 'user', 'machine_id',)
    ordering = ('process_name',)
    list_filter = ('process_name', 'user',)
