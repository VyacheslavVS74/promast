# Generated by Django 4.1.7 on 2023-06-26 19:02

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_remove_order_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
