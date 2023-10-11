from .forms import MessageForm
from django.contrib import messages
from django.shortcuts import redirect


def post_success(request):
    form = MessageForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, f"{request.POST.get('name')}")
        return redirect('main:success')
