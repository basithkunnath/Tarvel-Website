# Generated by Django 5.1.3 on 2024-11-16 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0021_rename_package_name_packages_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packages',
            old_name='title',
            new_name='packagetitle',
        ),
    ]
