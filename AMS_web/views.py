from django.shortcuts import render

# Create your views here.
def Home(requests):
	return render(requests, 'home.html',{})

def Download(requests):
	return render(requests, 'download.html', {})

def Documents(requests):
	return render(requests, 'Documents.html', {})

def Contact(requests):
	return render(requests, 'Contact.html', {})
