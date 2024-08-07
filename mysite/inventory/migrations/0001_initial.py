# Generated by Django 5.0.6 on 2024-07-08 07:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last name')),
            ],
        ),
        migrations.CreateModel(
            name='Decorations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('remaining', models.IntegerField(verbose_name='Remaining')),
                ('cost', models.FloatField(verbose_name='Cost')),
                ('price', models.FloatField(verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('remaining', models.IntegerField(verbose_name='Remaining')),
                ('cost', models.FloatField(verbose_name='Cost')),
                ('price', models.FloatField(verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='Silk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20, verbose_name='Color')),
                ('remaining', models.IntegerField(verbose_name='Remaining')),
                ('cost', models.FloatField(verbose_name='Cost')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.client')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField(verbose_name='Cost')),
                ('price', models.FloatField(verbose_name='Price')),
                ('materials_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.materials')),
                ('silk_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.silk')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(verbose_name='Quantity')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.client')),
                ('decorations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.decorations')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
    ]
