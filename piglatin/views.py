from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def translate(request):
	return HttpResponse("You are on translate page")