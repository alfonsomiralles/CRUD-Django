# Generated by Django 3.2.15 on 2022-11-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manytoone', '0003_remove_reporter_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporter',
            name='last_name',
            field=models.CharField(default='Apellido', max_length=80),
        ),
    ]
