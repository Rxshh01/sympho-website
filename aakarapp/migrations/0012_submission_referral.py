# Generated by Django 4.1 on 2023-12-21 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aakarapp', '0011_iitb_non_iitb'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='referral',
            field=models.CharField(default='NA', max_length=100),
            preserve_default=False,
        ),
    ]