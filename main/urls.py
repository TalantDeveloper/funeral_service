from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('service', views.service_view, name='service'),
    path('about', views.about_view, name='about'),
    path('contact', views.contact_view, name='contact'),
    path('success', views.success_view, name='success'),
    path('<str:name>', views.bad_url)
]