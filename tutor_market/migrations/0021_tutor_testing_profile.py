# Generated by Django 5.0.6 on 2024-09-02 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_market', '0020_tutor_profile_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='testing_profile',
            field=models.BooleanField(default=False),
        ),
    ]
