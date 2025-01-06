# Generated by Django 5.0.9 on 2025-01-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shift_assignment', '0006_completedshiftassignment_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completedshiftassignment',
            name='comment',
        ),
        migrations.AddField(
            model_name='completedshiftassignment',
            name='status',
            field=models.CharField(blank=True, choices=[('accepted', 'Продукция принята'), ('not_accepted', 'Продукция не принята')], max_length=20, null=True),
        ),
    ]