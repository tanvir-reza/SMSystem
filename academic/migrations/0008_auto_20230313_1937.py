# Generated by Django 3.2.13 on 2023-03-13 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0007_alter_class_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='obtained',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='total',
        ),
    ]
