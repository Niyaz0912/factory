# Generated by Django 5.0.9 on 2024-12-28 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process_history', '0008_auto_20241228_0423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processhistory',
            name='is_complete',
        ),
        migrations.AddField(
            model_name='processhistory',
            name='mark_yes_no',
            field=models.BooleanField(default=True, verbose_name='Отметка да/нет'),
        ),
    ]
