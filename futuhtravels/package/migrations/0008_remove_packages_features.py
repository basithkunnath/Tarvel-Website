# Generated by Django 5.1.3 on 2024-11-15 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0007_alter_packages_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packages',
            name='features',
        ),
    ]
