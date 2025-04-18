from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('catalog/', views.catalog, name='catalog'),
    path('categories/', views.categories, name='categories'),
    path('orders/', views.orders, name='orders'),
]
