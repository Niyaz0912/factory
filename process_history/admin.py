from django.contrib import admin
from .models import ProcessHistory


class ProcessHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'machine_id', 'part_id', 'batch_number', 'timestamp')


admin.site.register(ProcessHistory, ProcessHistoryAdmin)
