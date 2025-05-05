from django.shortcuts import render, get_object_or_404
from .models import Category, LegoSet


def home(request):
    categories = Category.objects.all()
    latest_sets = LegoSet.objects.all().order_by('-id')[:6]
    return render(request, 'legoshop/home.html', {
        'categories': categories,
        'latest_sets': latest_sets
    })


def categories(request):
    categories = Category.objects.all()
    return render(request, 'legoshop/categories.html', {'categories': categories})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    sets = LegoSet.objects.filter(category=category)
    return render(request, 'legoshop/category_detail.html', {
        'category': category,
        'sets': sets
    })


def product_detail(request, product_id):
    product = get_object_or_404(LegoSet, id=product_id)
    related_products = LegoSet.objects.filter(category=product.category).exclude(id=product.id)[:4]
    return render(request, 'legoshop/product_detail.html', {
        'product': product,
        'related_products': related_products
    })
