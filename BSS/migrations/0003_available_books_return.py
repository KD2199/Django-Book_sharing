# Generated by Django 3.0.2 on 2020-02-26 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BSS', '0002_remove_available_books_return'),
    ]

    operations = [
        migrations.AddField(
            model_name='available_books',
            name='Return',
            field=models.CharField(default='', max_length=25),
        ),
    ]
