# Generated by Django 4.2.5 on 2023-12-20 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
