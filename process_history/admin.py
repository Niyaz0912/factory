from django.contrib import admin
from process_history.models import ProcessHistory


@admin.register(ProcessHistory)
class ProcessHistoryAdmin(admin.ModelAdmin):
    list_display = ('process_name', 'detail_name', 'detail_quantity', 'user')  # Убедитесь, что используете только существующие поля
    ordering = ('timestamp',)  # Убедитесь, что это поле существует
    list_filter = ('user',)  # Убедитесь, что это поле существует
