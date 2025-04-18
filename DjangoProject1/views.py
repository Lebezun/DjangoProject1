from django.shortcuts import render


def home(request):
    """Головна сторінка"""
    return render(request, 'legoshop/home.html')


def about(request):
    """Сторінка про магазин"""
    return render(request, 'legoshop/about.html')


def catalog(request):
    """Сторінка каталогу"""
    return render(request, 'legoshop/catalog.html')


def categories(request):
    """Сторінка категорій"""
    return render(request, 'legoshop/categories.html')


def orders(request):
    """Сторінка замовлень"""
    return render(request, 'legoshop/orders.html')
