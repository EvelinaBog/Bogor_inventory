# Generated by Django 5.0.6 on 2024-07-09 19:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_alter_order_dec_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dec_price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.decorations'),
        ),
    ]