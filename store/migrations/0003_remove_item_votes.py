# Generated by Django 5.1.4 on 2025-01-17 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_wishlist_item_delete_choice_delete_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='votes',
        ),
    ]
