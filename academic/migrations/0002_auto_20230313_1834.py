# Generated by Django 3.2.13 on 2023-03-13 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='subjects',
        ),
        migrations.AddField(
            model_name='class',
            name='subjects',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academic.subject'),
        ),
    ]
