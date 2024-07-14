# Generated by Django 5.0.6 on 2024-07-13 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0030_remove_orderline_materials_remaining_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='decorationline',
            options={'verbose_name': 'Decoration Line', 'verbose_name_plural': 'Decoration Lines'},
        ),
        migrations.AlterModelOptions(
            name='decorations',
            options={'verbose_name': 'Decoration', 'verbose_name_plural': 'Decorations'},
        ),
        migrations.AlterModelOptions(
            name='materials',
            options={'verbose_name': 'Material', 'verbose_name_plural': 'Materials'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='orderline',
            options={'verbose_name': 'Order Line', 'verbose_name_plural': 'Order Lines'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='silk',
            options={'verbose_name': 'Silk', 'verbose_name_plural': 'Silks'},
        ),
        migrations.AlterModelOptions(
            name='wrappingpaper',
            options={'verbose_name': 'Wrapping Paper', 'verbose_name_plural': 'Wrapping Papers'},
        ),
    ]