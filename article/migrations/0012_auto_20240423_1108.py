# Generated by Django 2.2.13 on 2024-04-23 03:08

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20240411_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='body',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
