# Generated by Django 4.2.3 on 2023-07-12 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_colorvariant_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_desription',
            new_name='product_description',
        ),
    ]
