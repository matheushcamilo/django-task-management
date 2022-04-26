# Generated by Django 4.0.4 on 2022-04-26 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0002_alter_task_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='admin',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]