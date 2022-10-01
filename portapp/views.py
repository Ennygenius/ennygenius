from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages



# Create your views here.

def index(request):
	return render(request, 'portapp/index.html')

def about(request):
	return render(request, 'portapp/about.html')

def portfolio(request):
	return render(request, 'portapp/portfolio.html')

def home(request):
	return render(request, 'portapp/home.html')

def contact(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, ' Hi, f{username}, your request has be sent succesfully')
            return redirect('about.html')
    else:
        form = UserRegisterForm()

    return render(request, 'portapp/contact.html', {'form':form})