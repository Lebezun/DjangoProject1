from django.shortcuts import render
from .models import Category, LegoSet


def home(request):
    return render(request, 'legoshop/home.html')


def about(request):
    return render(request, 'legoshop/about.html')


def catalog(request):
    sets = LegoSet.objects.all()
    return render(request, 'legoshop/catalog.html', {'sets': sets})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'legoshop/categories.html', {'categories': categories})


def orders(request):
    return render(request, 'legoshop/orders.html')
