# Generated by Django 5.1.3 on 2024-11-14 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packages_image', models.ImageField(blank=True, null=True, upload_to='packages_images/')),
                ('packages_title', models.CharField(max_length=100)),
                ('packages_short_paragraph', models.CharField(max_length=1000)),
            ],
        ),
    ]