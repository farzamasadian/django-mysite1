from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)  
                return redirect('/')
            
        return render(request, 'accounts/login.html')
    else:
        return redirect('/')

@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')



def signup_view(request):
    return render(request, 'accounts/signup.html')