from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.contrib.auth.models import User

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'onlineshop/product/list.html', {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'onlineshop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})


def dashboard(request):
    _id = request.user
    user_id = _id.id
    users = get_object_or_404(User, id=user_id)
    return render(request, 'onlineshop/dash.html', {'users': users})


def search_function(request):
    if 'item' in request.GET:
        item_name = request.GET['item']
        products = Product.objects.all().filter(name__icontains=item_name)
    return render(request, 'onlineshop/product/list.html', {'products': products})

