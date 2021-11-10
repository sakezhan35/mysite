# Generated by Django 3.2.9 on 2021-11-06 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('description', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Планируется'), (1, 'Активная'), (2, 'Контроль'), (3, 'Завершена')], default=0)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('planned_end_time', models.DateTimeField()),
                ('observers', models.ManyToManyField(related_name='observers_tasks', to=settings.AUTH_USER_MODEL)),
                ('performer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performer_tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StatusChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_status', models.IntegerField(choices=[(0, 'Планируется'), (1, 'Активная'), (2, 'Контроль'), (3, 'Завершена')])),
                ('next_status', models.IntegerField(choices=[(0, 'Планируется'), (1, 'Активная'), (2, 'Контроль'), (3, 'Завершена')])),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_tracker.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
