from django.shortcuts import render, redirect
from .forms import NewForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('onlineshop:product_list')
        return render(request, 'accounts/register.html', {'register_form': form})
    form = NewForm()
    return render(request, 'accounts/register.html', {'register_form': form})

def login_req(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.info(request, f"You are now logged in as {username}.")
                return redirect('onlineshop:product_list')
            else:
                return render(request, 'accounts/login.html', {'login_form': form})
        else:
            return render(request, 'accounts/login.html', {'login_form': form})
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'login_form': form})

def logout_req(request):
    logout(request)
    return redirect('onlineshop:product_list')


