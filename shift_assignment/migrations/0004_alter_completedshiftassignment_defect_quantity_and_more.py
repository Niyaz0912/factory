# Generated by Django 5.0.9 on 2025-01-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shift_assignment', '0003_alter_completedshiftassignment_batch_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedshiftassignment',
            name='defect_quantity',
            field=models.IntegerField(default=0, verbose_name='Количество брака'),
        ),
        migrations.AlterField(
            model_name='completedshiftassignment',
            name='quantity',
            field=models.IntegerField(verbose_name='Количество'),
        ),
    ]