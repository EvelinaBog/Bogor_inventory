# Generated by Django 5.0.6 on 2024-07-09 05:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_remove_order_order_remove_orderline_client_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='client_id',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='decorations',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='product',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='qty',
        ),
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.client'),
        ),
        migrations.AddField(
            model_name='order',
            name='decorations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.decorations'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inventory.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='qty',
            field=models.IntegerField(default=0, verbose_name='Quantity'),
        ),
        migrations.AddField(
            model_name='orderline',
            name='client_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.client'),
        ),
    ]
