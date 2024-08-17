from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return render(request, 'registration/register.html', {'error': "Passwords don't match!"})
        else:
            my_user = User.objects.create_user(username, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'registration/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Debugging: Check what is being received
        print(f"Username: {username}")
        print(f"Password: {password}")

        user = authenticate(request, username=username, password=password)
        
        # Debugging: Check if user is authenticated
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'index')
            return redirect(next_url)
        else:
            # Debugging: Check if this part is reached
            print("Invalid credentials")
            return render(request, 'registration/login.html', {'error': "Invalid username or password!"})

    return render(request, 'registration/login.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('/')
