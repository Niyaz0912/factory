# Generated by Django 5.0.9 on 2025-01-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process_history', '0002_remove_processhistory_detail_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processhistory',
            name='batch_number',
            field=models.CharField(max_length=100, verbose_name='Наименование изделия'),
        ),
        migrations.AlterField(
            model_name='processhistory',
            name='part_id',
            field=models.CharField(max_length=100, verbose_name='№ партии'),
        ),
    ]