# Generated by Django 4.2.3 on 2023-07-09 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='test', max_length=100, unique=True),
        ),
    ]