# Generated by Django 5.0.9 on 2024-11-09 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_telegram_user_username_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='active'),
        ),
    ]
