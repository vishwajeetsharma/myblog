# Generated by Django 3.2.7 on 2021-12-29 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211229_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='category',
        ),
    ]
