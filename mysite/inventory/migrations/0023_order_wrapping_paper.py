# Generated by Django 5.0.6 on 2024-07-10 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0022_delete_profit'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='wrapping_paper',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.materials'),
        ),
    ]