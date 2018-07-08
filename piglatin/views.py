from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def translate(request):
	original = request.GET['originalText'].lower()
	#splits the string about ' '
	list = original.split()
	translation = ""

	for word in list:
		if(word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u'):
			translation+=word+"yay "
		else:
			translation+=word[1:]
			translation+=word[0]+"yay "

    #values can be passed on to .html using this dictionary where key can be named anything and is used in .html 
    #value is what we are concerned about
	return render(request, 'translate.html', {'original':original, 'translation':translation})