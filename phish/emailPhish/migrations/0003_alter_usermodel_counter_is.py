# Generated by Django 4.2.1 on 2023-05-26 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailPhish', '0002_remove_usermodel_status_usermodel_counter_is_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='counter_is',
            field=models.IntegerField(default=0),
        ),
    ]
