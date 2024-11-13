# Generated by Django 5.0.9 on 2024-11-10 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process_history', '0003_shiftassignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='processhistory',
            name='machine_id',
            field=models.IntegerField(default=1, verbose_name='ID станка'),
        ),
        migrations.AddField(
            model_name='processhistory',
            name='process_name',
            field=models.CharField(default='Процесс ...', max_length=255),
        ),
    ]