# Generated by Django 4.1.5 on 2023-01-31 04:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_assignments_assignment_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserClassData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=8)),
                ('class_id', models.CharField(max_length=8)),
            ],
        ),
        migrations.RemoveField(
            model_name='classes',
            name='id',
        ),
        migrations.AlterField(
            model_name='assignments',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2023, 1, 30, 20, 15, 43, 523609)),
        ),
        migrations.AlterField(
            model_name='classes',
            name='class_id',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]
