from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout

from django.contrib import messages

from .forms import UserForm, UserProfileForm


def home(request):
    return render(request, 'users/home.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def register(request):
    form_user=UserForm()
    form_profile = UserProfileForm()
    context={
        'form_profile':form_profile,
        'form_user':form_user,
    }

    return render(request, 'users/register.html', context)