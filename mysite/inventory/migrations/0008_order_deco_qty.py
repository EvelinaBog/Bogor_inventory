# Generated by Django 5.0.6 on 2024-07-09 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_remove_order_client_id_remove_orderline_decorations_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deco_qty',
            field=models.IntegerField(default=0, verbose_name='Quantity'),
        ),
    ]