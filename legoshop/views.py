from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def catalog(request):
    return render(request, 'catalog.html')


def promotions(request):
    return render(request, 'promotions.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')
