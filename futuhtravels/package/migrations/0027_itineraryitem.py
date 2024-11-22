# Generated by Django 5.1.3 on 2024-11-16 05:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0026_view_all_packages_features'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItineraryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_number', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itinerary_items', to='package.view_all_packages')),
            ],
        ),
    ]
