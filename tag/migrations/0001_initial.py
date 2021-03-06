# Generated by Django 3.1.7 on 2021-03-05 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Tag Name')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='Registered Date/Time')),
            ],
            options={
                'verbose_name': 'byun_project_tag',
                'db_table': 'byun_project_tags',
            },
        ),
    ]
