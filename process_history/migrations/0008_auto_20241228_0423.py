from django.db import migrations


def fill_roughness_check(apps, schema_editor):
    ProcessHistory = apps.get_model('process_history', 'ProcessHistory')  # Замените your_app_name на my_app
    for record in ProcessHistory.objects.all():
        record.roughness_check = '+'  # Или другое значение по умолчанию
        record.save()


class Migration(migrations.Migration):
    dependencies = [
        ('process_history', '0007_processhistory_defects_check_and_more'),  # Укажите правильную зависимость
    ]

    operations = [
        migrations.RunPython(fill_roughness_check),
    ]
