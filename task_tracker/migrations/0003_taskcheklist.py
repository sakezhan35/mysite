# Generated by Django 3.2.9 on 2021-11-06 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0002_reminder'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskChekList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('is_completed', models.BooleanField(default=False)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_tracker.task')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
