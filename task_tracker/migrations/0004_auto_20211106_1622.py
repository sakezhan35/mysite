# Generated by Django 3.2.9 on 2021-11-06 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0003_taskcheklist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='end_time',
            new_name='end_datetime',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='planned_end_time',
            new_name='planned_end_datetime',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='start_time',
            new_name='start_datetime',
        ),
    ]