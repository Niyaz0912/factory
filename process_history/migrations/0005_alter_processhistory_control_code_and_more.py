# Generated by Django 5.0.9 on 2025-01-05 19:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process_history', '0004_saveprocesshistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processhistory',
            name='control_code',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('3;2', '3;2')], default='1', max_length=10, verbose_name='Код контроля'),
        ),
        migrations.AlterField(
            model_name='processhistory',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(21.95), django.core.validators.MaxValueValidator(22)], verbose_name='Значение специальной характеристики'),
        ),
    ]
