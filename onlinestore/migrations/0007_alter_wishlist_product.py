# Generated by Django 4.2.4 on 2023-10-10 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinestore', '0006_alter_wishlist_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='product',
            field=models.IntegerField(max_length=60, unique=True),
        ),
    ]
