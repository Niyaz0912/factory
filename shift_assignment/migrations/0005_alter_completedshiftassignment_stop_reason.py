# Generated by Django 5.0.9 on 2025-01-03 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shift_assignment', '0004_alter_completedshiftassignment_defect_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedshiftassignment',
            name='stop_reason',
            field=models.TextField(blank=True, null=True, verbose_name='Причина остановки станка'),
        ),
    ]