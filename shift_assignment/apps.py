from django.apps import AppConfig


class ShiftAssignmentConfig(AppConfig):
    """
    Конфигурация приложения 'shift_assignment'.

    Этот класс настраивает параметры приложения, такие как
    имя приложения и тип автоинкрементного поля по умолчанию.
    """

    # Указывает тип поля для автоинкрементации по умолчанию
    default_auto_field = 'django.db.models.BigAutoField'

    # Имя приложения, используемое в проекте
    name = 'shift_assignment'

