# Generated by Django 4.2.3 on 2023-07-19 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_product_desription_product_product_description'),
        ('order', '0003_alter_cartitem_cart_alter_cartitem_item_count'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart', 'product')},
        ),
    ]