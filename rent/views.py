from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import room

def homepage(request):
    return render(request, 'rent/index.html')

def register(request):  
    if request.method == 'POST':
        Username = request.POST['username']
        Email = request.POST['email']
        Password1 = request.POST['password1']
        Password2 = request.POST['password2']

        if Password1 == Password2:
            if User.objects.filter(username = Username).exists():
                messages.error(request, 'Username is taken!')
                return redirect('signup')
            elif User.objects.filter(email = Email).exists():
                messages.error(request, 'Email is taken!')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=Username, email=Email, password=Password1)
                user.save()
                messages.success(request, 'User created!')
                return redirect('login')
        else:
            messages.error(request, 'Passwords not matching!')
            return redirect('signup')
    else:   
        return render(request,'rent/register.html')

def user_login(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Password = request.POST['password']
        user = auth.authenticate(username=Username,password=Password)
        if user is not None:
            auth.login(request,user)
            return redirect('search')
        else:
            messages.error(request, 'Invalid credentials' ) 
            return redirect('login')  
    else:
        return render(request, 'rent/login.html')

def user_logout(request):
    auth.logout(request) 
    #messages.info(request, "Logged out successfully!")
    return redirect('index')

def booking(request):
    return render(request, 'rent/booking.html')

def payment(request):
    return render(request, 'rent/payment.html')

def rooms(request):
    if request.method == "POST":
        city = request.POST['city']
        display = room.objects.filter(city = city)
        view = list(display)
        context = {'display': view}
        return render(request, 'rent/room.html', context)
    else:
        return render(request, 'rent/room.html')
