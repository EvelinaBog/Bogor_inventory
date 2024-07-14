# Generated by Django 5.0.6 on 2024-07-08 12:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_remove_orderline_decorations_orderline_decorations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='client_id',
        ),
        migrations.AddField(
            model_name='orderline',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.order'),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='decorations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.decorations'),
        ),
    ]
