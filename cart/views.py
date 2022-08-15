from django.shortcuts import render, get_object_or_404, redirect
from onlineshop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import UserAddress

@require_POST       # to allow post request
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

@login_required(login_url='accounts:login')
def cart_detail(request):       # get current cart and display
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

def checkout(request):

    if request.method == 'POST':
        items = request.POST.get('products')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        price = request.POST.get('price')
        cod = request.POST.get('payment')

        myaddress = UserAddress(items=items, name=name, email=email, address=address, contact=contact, city=city, state=state, zip=zip, price=price, cash_on_delivery=cod)
        myaddress.save()
        return render(request, 'cart/placed.html')

