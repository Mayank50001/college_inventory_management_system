# Generated by Django 5.1.4 on 2025-03-24 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_login_device',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
