# Generated by Django 4.2.4 on 2023-08-31 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_location_country'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='user_location',
            constraint=models.UniqueConstraint(models.F('user_id'), models.F('location_id'), name='user_location_unique', violation_error_message='This City was already added to specified user'),
        ),
    ]
