# Generated by Django 5.0.6 on 2024-07-08 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_product_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderline',
            name='decorations',
        ),
        migrations.AddField(
            model_name='orderline',
            name='decorations',
            field=models.ManyToManyField(to='inventory.decorations'),
        ),
    ]