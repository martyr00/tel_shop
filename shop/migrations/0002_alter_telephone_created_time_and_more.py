# Generated by Django 4.2.7 on 2023-11-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telephone',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='telephone',
            name='update_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
