from django.contrib import admin
from .models import Message, Service


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    class Meta:
        modul = Message
        fields = '__all__'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    class Meta:
        model = Service
        fields = '__all__'
