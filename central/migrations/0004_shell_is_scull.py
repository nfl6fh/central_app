# Generated by Django 4.2.5 on 2023-12-20 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0003_lineup_workout'),
    ]

    operations = [
        migrations.AddField(
            model_name='shell',
            name='is_scull',
            field=models.BooleanField(default=False),
        ),
    ]
