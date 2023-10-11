from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Message, Service, Client
from .forms import MessageForm
from .function import post_success


def welcome_view(request):
    services = Service.objects.all()
    clients = Client.objects.all()
    if request.method == 'POST':
        return post_success(request)
    return render(request, 'main/welcome.html', {'services': services, 'clients': clients})


def service_view(request):
    services = Service.objects.all()

    return render(request, 'main/service.html', {'services': services})


def about_view(request):
    return render(request, 'main/about.html')


def contact_view(request):
    if request.method == 'POST':
        return post_success(request)
    return render(request, 'main/contact.html')


def success_view(request):
    return render(request, 'main/success.html')
