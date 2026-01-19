from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import Product


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('products')
        else:
            return render(request, 'login.html', {'error': 'Неверный логин или пароль'})

    return render(request, 'login.html')


def guest_login(request):
    request.session['is_guest'] = True
    return redirect('products')


def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('login')


def products_view(request):
    products = Product.objects.select_related(
        'category',
        'manufacturer',
        'supplier',
    ).all()
    
    user_fio = None
    
    if request.user.is_authenticated:
        user_fio = request.user.get_full_name()
    elif request.session.get('is_guest', False):
        user_fio = "Гость"

    context = {
        'products': products,
        'user_fio': user_fio,
        'user': request.user,
    }

    return render(request, 'products.html', context)
