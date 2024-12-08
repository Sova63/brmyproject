from django.shortcuts import render


def index(request):
	return render(request,'news/index.html')

def newsfirst(request):
	return render(request, 'news/newsfirst.html')
