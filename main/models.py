from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ваше имя")
    number = models.CharField(max_length=50, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Почта")
    message = models.TextField(verbose_name="Сообщение")

    def __str__(self):
        return self.name
