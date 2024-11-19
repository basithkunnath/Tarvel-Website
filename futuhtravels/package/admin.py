from django.contrib import admin
from .models import view_all_packages
from .models import ItineraryItem
# Register your models here.



admin.site.register(view_all_packages)
admin.site.register(ItineraryItem)