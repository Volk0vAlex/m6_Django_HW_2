from django.urls import path
from . import views

from catalog.views import home, contacts
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home, name='list'),
    path('contacts/<int:id>', views.contacts, name='details')
]
