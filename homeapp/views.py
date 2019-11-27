from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')

def modernmarket(request):
    return render(request, 'm_market.html')

def modernadvertising(request):
    return render(request, 'm_advertising.html')

def modernresearch(request):
    return render(request, 'm_research.html')

def moderncare(request):
    return render(request, 'm_care.html')

def modernengage(request):
    return render(request, 'm_engage.html')

def integrationapis(request):
    return render(request, 'i_api.html')

def partner(request):
    return render(request, 'partner.html')

def training(request):
    return render(request, 'training.html')

def agency(request):
    return render(request, 'agency.html')

def customer(request):
    return render(request, 'customer.html')