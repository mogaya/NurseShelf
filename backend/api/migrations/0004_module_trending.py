# Generated by Django 5.1.5 on 2025-03-04 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_subscription_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='trending',
            field=models.BooleanField(default=False),
        ),
    ]
