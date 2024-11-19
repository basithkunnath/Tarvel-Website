from django.urls import path
from . import views
urlpatterns = [
   path('packages/', views.packages, name='packages'),
   path('package_details/<int:pk>/', views.package_details, name='package_details')
]   