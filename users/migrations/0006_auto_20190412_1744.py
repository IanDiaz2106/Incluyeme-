# Generated by Django 2.2 on 2019-04-12 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='rut',
            field=models.CharField(max_length=150),
        ),
    ]
