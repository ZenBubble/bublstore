# Generated by Django 5.1.4 on 2025-01-17 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_item_votes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='cart',
            new_name='wishlist',
        ),
    ]
