# Generated by Django 3.2.13 on 2023-03-13 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_auto_20230313_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='subjects',
        ),
        migrations.AddField(
            model_name='class',
            name='subjects',
            field=models.ManyToManyField(to='academic.Subject'),
        ),
    ]
