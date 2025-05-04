from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

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
    
def logout_view(request):
    return render(request, 'accounts/logout.html')

def signup_view(request):
    return render(request, 'accounts/signup.html')