import pandas as pd
from process_history.models import ProcessHistory

def export_to_excel(file_path):
    # Извлечение всех записей из модели ProcessHistory
    data = ProcessHistory.objects.all().values(
        'process_name',
        'detail_name',
        'user__username',  # Если у вас есть связь с пользователем
        'machine_id',
        'parameter_name',
        'value',
        'timestamp',
        'detail_quantity',
        'assignment__id',  # Если у вас есть связь со сменным заданием
        'is_complete',
        'control_code',
        'roughness_check',
        'defects_check',
        'threading_check',
        'diameter_check'
    )

    # Создание DataFrame из данных
    df = pd.DataFrame(list(data))

    # Преобразование временных меток в наивные datetime
    if 'timestamp' in df.columns:
        df['timestamp'] = df['timestamp'].dt.tz_localize(None)  # Убираем информацию о часовом поясе

    # Сохранение DataFrame в Excel
    df.to_excel(file_path, index=False)
