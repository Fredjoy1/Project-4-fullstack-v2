# Generated by Django 3.2.15 on 2022-08-21 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Welcome to Code Zone', max_length=255),
        ),
    ]
