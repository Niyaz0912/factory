# Generated by Django 5.0.9 on 2024-12-29 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process_history', '0011_alter_processhistory_control_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='processhistory',
            name='is_complete',
            field=models.BooleanField(default=False, verbose_name='Завершено'),
        ),
    ]