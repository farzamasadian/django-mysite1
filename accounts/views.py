from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
import inspect

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Logged in successfully as {username}!', extra_tags='login-success')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password.', extra_tags='login-error')
                return render(request, 'accounts/login.html') # Re-render with error message

        return render(request, 'accounts/login.html')
    else:
        return redirect('/')

@login_required
def logout_view(request):
    if request.user.is_authenticated:
        messages.info(request, 'Logged out successfully.', extra_tags='logout-success')
        logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            print("The CustomUserCreationForm is being loaded from this file:", inspect.getfile(CustomUserCreationForm))
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created successfully for {username}! Please log in.', extra_tags='signup-success')
                return redirect('/accounts/login')
            else:
                print("Form is not valid. Errors:", form.errors)

                context = {'form': form}
                return render(request, 'accounts/signup.html', context)

        form = CustomUserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context=context)
    else:
        return redirect('/')