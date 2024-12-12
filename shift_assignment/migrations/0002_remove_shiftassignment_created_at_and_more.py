# Generated by Django 5.0.9 on 2024-12-12 14:36

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shift_assignment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shiftassignment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='shiftassignment',
            name='master',
        ),
        migrations.AddField(
            model_name='shiftassignment',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='shiftassignment',
            name='batch_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='shiftassignment',
            name='machine_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='shiftassignment',
            name='operation_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='shiftassignment',
            name='operator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shiftassignment',
            name='part_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='shiftassignment',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
