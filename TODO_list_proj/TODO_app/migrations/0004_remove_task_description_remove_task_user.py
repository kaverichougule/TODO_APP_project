# Generated by Django 4.0.5 on 2022-06-21 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TODO_app', '0003_task_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]