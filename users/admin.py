from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name', 'role', 'pk', 'is_active')
    list_filter = ('last_name', 'is_active')  # Добавлено поле is_active для фильтрации
    search_fields = ('username', 'last_name', 'first_name')  # Добавлена возможность поиска
    ordering = ('last_name', 'first_name')  # Установлена сортировка по умолчанию
