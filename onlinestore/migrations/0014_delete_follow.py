# Generated by Django 4.2.4 on 2023-10-27 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinestore', '0013_alter_comments_product_alter_wishlist_product_follow'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
