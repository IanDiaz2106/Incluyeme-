# Generated by Django 2.2 on 2019-04-13 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_administrador_edad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrador',
            name='edad',
        ),
    ]