# Generated by Django 4.1.5 on 2023-01-16 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.CharField(max_length=8)),
                ('class_subject', models.CharField(max_length=12)),
                ('class_name', models.CharField(max_length=30)),
                ('teacher_name', models.CharField(max_length=30)),
                ('assignments_due', models.IntegerField()),
            ],
        ),
    ]
