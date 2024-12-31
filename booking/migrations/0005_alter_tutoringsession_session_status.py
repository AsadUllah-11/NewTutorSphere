# Generated by Django 5.0.6 on 2024-07-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_payment_client_secret_payment_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutoringsession',
            name='session_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled'), ('rescheduled', 'Rescheduled')], default='pending', max_length=20),
        ),
    ]
