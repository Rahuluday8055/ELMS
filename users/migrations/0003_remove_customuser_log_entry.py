# Generated by Django 5.1.6 on 2025-03-19 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_log_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='log_entry',
        ),
    ]
