# Generated by Django 3.1.7 on 2021-05-07 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210505_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, default='header.jpg', null=True, upload_to='header_pictures'),
        ),
    ]