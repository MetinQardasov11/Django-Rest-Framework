# Generated by Django 5.1.4 on 2025-01-24 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterModelOptions(
            name='profilestatus',
            options={'verbose_name_plural': 'Profile Statuses'},
        ),
    ]
