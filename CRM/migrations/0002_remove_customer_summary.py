# Generated by Django 4.2.3 on 2023-08-05 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='summary',
        ),
    ]