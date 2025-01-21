import pandas as pd
from process_history.models import ProcessHistory


def export_to_excel(file_path):
    """
    Экспортирует данные из модели ProcessHistory в файл Excel.

    Параметры:
    file_path (str): Путь к файлу, в который будут сохранены данные.
    """

    # Извлечение всех записей из модели ProcessHistory
    data = ProcessHistory.objects.all().values(
        'process_name',
        'detail_name',
        'user__username',  # Имя пользователя, если есть связь с пользователем
        'machine_id',
        'parameter_name',
        'value',
        'timestamp',
        'detail_quantity',
        'assignment__id',  # ID сменного задания, если есть связь
        'is_complete',
        'control_code',
        'roughness_check',
        'defects_check',
        'threading_check',
        'diameter_check'
    )

    # Создание DataFrame из извлеченных данных
    df = pd.DataFrame(list(data))

    # Преобразование временных меток в наивные datetime (без информации о часовом поясе)
    if 'timestamp' in df.columns:
        df['timestamp'] = df['timestamp'].dt.tz_localize(None)  # Убираем информацию о часовом поясе

    # Сохранение DataFrame в файл Excel
    df.to_excel(file_path, index=False)

