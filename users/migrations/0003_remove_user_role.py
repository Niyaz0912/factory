# Generated by Django 5.0.9 on 2024-11-10 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_role_user_username_alter_user_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
