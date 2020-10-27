
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *


def cour(request):
    cours = Cour.objects.all()
    context = {'cours':cours}
    return render(request, 'Files/docfiles.html', context)
def exercice(request):
    exercices = Exercice.objects.all()
    context = {'exercices':exercices}
    return render(request, 'Files/exercices.html', context)
def correction(request):
    corrigés = Corrigé.objects.all()
    context = {'corrigés':corrigés}
    return render(request, 'Files/correction.html', context)
  
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('cour')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('cour')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('cour')
			else:
	 			messages.info(request, 'Username OR password is incorrect')
		context = {}
		return render(request, 'Files/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def classe(request):
    classes = Classe.objects.all()
    context = {'classes':classes}
    return render(request, 'Files/Live.html', context)
def live(request):
    lives = Live_ended.objects.all()
    context = {'lives':lives}
    return render(request, 'Files/endlives.html', context)
  
