# Generated by Django 3.1.7 on 2021-05-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210504_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.TextField(default='uncategorized', max_length=255),
        ),
    ]
