# Generated by Django 4.2.5 on 2023-12-20 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0002_user_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineup',
            name='workout',
            field=models.CharField(default='', max_length=300),
        ),
    ]