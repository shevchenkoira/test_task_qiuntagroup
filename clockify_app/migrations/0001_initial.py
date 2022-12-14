# Generated by Django 4.0.4 on 2022-10-27 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParsingHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=100, verbose_name='Username')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('status', models.CharField(max_length=25, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'User',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=100, verbose_name='Task name')),
                ('status', models.CharField(max_length=25, verbose_name='Status')),
                ('project_name', models.CharField(default='None', max_length=200, verbose_name='Project name')),
                ('start_time', models.DateTimeField(verbose_name='Start time')),
                ('end_time', models.DateTimeField(verbose_name='End time')),
                ('duration', models.CharField(max_length=50, verbose_name='Duration')),
                ('start_date', models.DateField(default='2000-01-01', verbose_name='Start date')),
                ('end_date', models.DateField(default='2000-01-01', verbose_name='End date')),
                ('assignees', models.ManyToManyField(to='clockify_app.user')),
            ],
            options={
                'verbose_name': 'Task',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=100, verbose_name='Project name')),
                ('archived', models.BooleanField(verbose_name='Archived')),
                ('public', models.BooleanField(verbose_name='Public')),
                ('tasks', models.ManyToManyField(to='clockify_app.task')),
            ],
            options={
                'verbose_name': 'Project',
            },
        ),
    ]
