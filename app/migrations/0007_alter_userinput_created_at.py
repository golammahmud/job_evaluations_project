# Generated by Django 3.2.3 on 2021-09-24 10:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_userinput_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinput',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
