# Generated by Django 4.2.1 on 2023-06-03 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_alter_todoappmodel_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoappmodel',
            old_name='completed_time',
            new_name='completed_on_datetime',
        ),
    ]