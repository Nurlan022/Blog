# Generated by Django 3.1.7 on 2021-05-07 09:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210505_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_day',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
