from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    class Meta:
        modul = Message
        fields = '__all__'
