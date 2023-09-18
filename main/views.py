from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm


def welcome_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:success')
    return render(request, 'main/welcome.html')


def service_view(request):
    return render(request, 'main/service.html')


def about_view(request):
    return render(request, 'main/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:success')
    return render(request, 'main/contact.html')


def success_view(request):
    return render(request, 'main/success.html')
