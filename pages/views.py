from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request, 'pages/index.html')

def about(request):
  return render(request, 'pages/about-us.html')

def services(request):
  return render(request, 'pages/services.html')

def contact(request):
  return render(request, 'pages/contact-us.html')


