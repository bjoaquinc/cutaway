from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'website/home.html')

def work(request):
    return render(request, 'website/work.html', {'title': 'Work'})

def trust(request):
    return render(request, 'website/trust.html', {'title': 'Trust'})

def contact(request):
    return render(request, 'website/contact.html', {'title': 'Contact Us'})