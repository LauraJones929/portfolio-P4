# Generated by Django 3.2.13 on 2022-06-15 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Membership',
            new_name='Product',
        ),
    ]
