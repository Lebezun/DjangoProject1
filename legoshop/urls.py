from django.urls import path
from . import views

app_name = 'legoshop'  # Додайте цей рядок

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('promotions/', views.promotions, name='promotions'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]
