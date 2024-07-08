# Generated by Django 4.2.5 on 2023-10-11 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('image', models.ImageField(default='./image/avatar.png', upload_to='./user/')),
                ('content', models.TextField(verbose_name='содержание')),
            ],
        ),
    ]