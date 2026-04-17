from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.middleware.csrf import rotate_token
from django.http import HttpResponse
from .forms import RegisterForm
from vehicles.models import Vehicle

def home_view(request):
    total_vehicles = Vehicle.objects.count()
    most_expensive = Vehicle.objects.order_by('-price').first()
    context = {
        'total_vehicles': total_vehicles,
        'most_expensive': most_expensive,
    }
    return render(request, 'users/home.html', context)

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        rotate_token(request)
        return redirect('home')
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            rotate_token(request)
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

# --- EMERGENCY LOGIN FIX ---
def create_admin_emergency(request):
    User = get_user_model()
    username = 'sauce'
    password = '50361Pay'
    
    # This creates the user 'sauce' in your Neon database
    user, created = User.objects.get_or_create(username=username)
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    
    if created:
        return HttpResponse(f"✅ Created superuser: {username}")
    return HttpResponse(f"🔄 Reset password for: {username}")