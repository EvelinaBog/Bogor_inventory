# Generated by Django 5.0.6 on 2024-07-09 06:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_order_deco_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderline',
            name='order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='order_lines', to='inventory.order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='deco_qty',
            field=models.IntegerField(default=0, verbose_name='Decoration Quantity'),
        ),
    ]
