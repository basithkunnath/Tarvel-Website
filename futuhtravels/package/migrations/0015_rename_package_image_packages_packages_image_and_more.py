# Generated by Django 5.1.3 on 2024-11-16 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0014_alter_packages_package_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packages',
            old_name='package_image',
            new_name='packages_image',
        ),
        migrations.RemoveField(
            model_name='packages',
            name='package_shot_description',
        ),
        migrations.RemoveField(
            model_name='packages',
            name='package_title',
        ),
        migrations.AddField(
            model_name='packages',
            name='country_name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='packages',
            name='duration',
            field=models.CharField(max_length=26, null=True),
        ),
        migrations.AddField(
            model_name='packages',
            name='features',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='packages',
            name='packages_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='packages',
            name='packages_sub_image_1',
            field=models.ImageField(blank=True, null=True, upload_to='package_images/'),
        ),
        migrations.AddField(
            model_name='packages',
            name='packages_sub_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='package_images/'),
        ),
        migrations.AddField(
            model_name='packages',
            name='packages_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
