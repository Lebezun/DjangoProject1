from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, LegoSet, Order


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


def order_create(request, product_id):
    product = get_object_or_404(LegoSet, id=product_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        if not (name and email and phone):
            error = "Будь ласка, заповніть усі поля."
            return render(request, 'legoshop/order_form.html', {
                'product': product,
                'error': error,
                'quantity': quantity,
                'name': name,
                'email': email,
                'phone': phone,
            })

        order = Order.objects.create(
            lego_set=product,
            quantity=quantity,
            customer_name=name,
            customer_email=email,
            customer_phone=phone
        )
        return redirect('order_success', order_id=order.id)

    # GET — перевіряємо чи є параметр quantity в GET, щоб попередньо заповнити форму
    quantity = int(request.GET.get('quantity', 1))
    return render(request, 'legoshop/order_form.html', {
        'product': product,
        'quantity': quantity,
    })


def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'legoshop/order_success.html', {'order': order})
