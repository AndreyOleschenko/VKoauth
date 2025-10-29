from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token

# Create your views here.
def home_view(request):
    return render(request, template_name='home.html')

def login_view(request):
    if request.method == 'POST':
        # Pass request to AuthenticationForm so it can perform request-aware validation
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # AuthenticationForm already validates credentials; get authenticated user
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, template_name='login.html', context={'form': form})

def signin_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, template_name='signin.html', context={'form': form}) 


def logout_view(request):
    logout(request)
    return redirect('home')