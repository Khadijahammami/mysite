from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.decorators import login_required
def index(request):
    context = {'val':"Menu Acceuil"}
    return render(request, 'acceuil.html',context)
@login_required
def home(request):
    context = {'val':"Menu Acceuil"}
    return render(request, 'acceuil.html',context)
