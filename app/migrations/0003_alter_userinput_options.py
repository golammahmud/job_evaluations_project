# Generated by Django 3.2.3 on 2021-09-23 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210923_2114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinput',
            options={'ordering': ['-number']},
        ),
    ]
