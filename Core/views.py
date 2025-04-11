from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import User



def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        r_password = request.POST.get('r_password')
        if password != r_password:
            messages.error(request, 'пароли не совпадают')
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'имя занято')
            return redirect('signup')
        
        User.objects.create_user(username=username, password=password)
        return redirect('signin')

    return render(request, 'Core/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if not user:
            return redirect('signin')
        
        login(request, user)
        return redirect('profile')
    
    return render(request, 'Core/signin.html')

def profile(request):
    user = request.user
    return render(request, 'Core/profile.html', {'user': user})

def signout(request):
    logout(request)
    return redirect('kinopoisk:main')