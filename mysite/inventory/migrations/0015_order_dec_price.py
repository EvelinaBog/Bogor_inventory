# Generated by Django 5.0.6 on 2024-07-09 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_alter_decorations_cost_alter_decorations_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='dec_price',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='inventory.decorations'),
        ),
    ]
