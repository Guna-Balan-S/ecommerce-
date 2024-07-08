from django.shortcuts import render, redirect
from.models import Product, Order
from.forms import ProductForm, OrderForm
from django.contrib.auth.decorators import login_required

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})

@login_required
def add_to_cart(request, pk):
    product = Product.objects.get(pk=pk)
    order = Order(user=request.user, product=product, quantity=1)
    order.save()
    return redirect('cart')

@login_required
def cart(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'cart.html', {'orders': orders})

@login_required
def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('order_tracking')
    else:
        form = OrderForm()
    return render(request, 'checkout.html', {'form': form})

@login_required
def order_tracking(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_tracking.html', {'orders': orders})