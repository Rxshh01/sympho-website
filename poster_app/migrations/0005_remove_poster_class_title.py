# Generated by Django 4.1 on 2023-02-06 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poster_app', '0004_poster_class_experience_poster_class_ref'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poster_class',
            name='title',
        ),
    ]