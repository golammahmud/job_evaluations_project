# Generated by Django 3.2.3 on 2021-09-25 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_userinput_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinput',
            options={'ordering': ['-created_at']},
        ),
    ]
