# Generated by Django 5.0.9 on 2024-12-27 23:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process_history', '0006_processhistory_control_code'),
        ('shift_assignment', '0003_remove_shiftassignment_master_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='processhistory',
            name='defects_check',
            field=models.CharField(choices=[('+', '+'), ('-', '-')], default='+', max_length=1, verbose_name='Отсутствие рисок, канавок и т.д.'),
        ),
        migrations.AddField(
            model_name='processhistory',
            name='diameter_check',
            field=models.CharField(choices=[('+', '+'), ('-', '-')], default='+', max_length=1, verbose_name='Диаметр галтели'),
        ),
        migrations.AddField(
            model_name='processhistory',
            name='roughness_check',
            field=models.CharField(choices=[('+', '+'), ('-', '-')], default='+', max_length=1, verbose_name='Шероховатость'),
        ),
        migrations.AddField(
            model_name='processhistory',
            name='threading_check',
            field=models.CharField(choices=[('+', '+'), ('-', '-')], default='+', max_length=1, verbose_name='Наличие резьбы и отверстия под шплинт'),
        ),
        migrations.AlterField(
            model_name='processhistory',
            name='assignment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shift_assignment.shiftassignment', verbose_name='Сменное задание'),
        ),
        migrations.AlterField(
            model_name='processhistory',
            name='control_code',
            field=models.CharField(choices=[('1', 'Код 1'), ('2', 'Код 2'), ('3', 'Код 3'), ('4', 'Код 4'), ('5', 'Код 5'), ('6', 'Код 6'), ('3;2', 'Код 3;2')], max_length=10, verbose_name='Код контроля'),
        ),
        migrations.AlterField(
            model_name='processhistory',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Оператор'),
        ),
    ]
