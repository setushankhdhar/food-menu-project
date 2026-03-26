from django.shortcuts import render,HttpResponse, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}! Your account is successfully created.')
            return redirect('users:login')
    return render(request,'users/register.html',{"form":form})

def logout_view(request):
    logout(request)
    return render(request,'users/logout.html')

@login_required
def profile(request):
    return render(request,'users/profile.html')