# Generated by Django 5.1.3 on 2024-11-16 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0013_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='package_image',
            field=models.ImageField(blank=True, null=True, upload_to='packages_images/'),
        ),
    ]
