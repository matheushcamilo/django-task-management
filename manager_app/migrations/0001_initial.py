# Generated by Django 4.0.4 on 2022-04-26 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('task_type', models.CharField(choices=[('PV', 'Primeira Visita'), ('SV', 'Segunda Visita'), ('D', 'Discurso'), ('DP', 'Discurso Público')], max_length=2)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager_app.person')),
            ],
        ),
    ]
