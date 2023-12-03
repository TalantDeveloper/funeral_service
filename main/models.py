from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ваше имя")
    number = models.CharField(max_length=50, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Почта")
    message = models.TextField(verbose_name="Сообщение")

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=300, verbose_name='сервис')
    content = models.TextField(verbose_name='content')
    image = models.ImageField(upload_to='./image/')

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    image = models.ImageField(upload_to='./user/', default='./image/avatar.png')
    content = models.TextField(verbose_name='содержание')

    def __str__(self):
        return self.name
