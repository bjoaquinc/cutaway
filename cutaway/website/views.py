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

def conceptualization(request):
    return render(request, 'website/conceptualization.html', {'title': 'Conceptualization'})

def creation(request):
    return render(request, 'website/creation.html', {'title': 'Creation'})

def delivery(request):
    return render(request, 'website/delivery.html', {'title': 'Delivery'})
