# Generated by Django 5.1.3 on 2024-11-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0004_alter_packages_features_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='features',
            field=models.JSONField(),
        ),
    ]
