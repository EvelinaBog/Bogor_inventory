from django.db import models


class Silk(models.Model):
    color = models.CharField(verbose_name='Color', max_length=20)
    remaining = models.FloatField(verbose_name='Remaining', default=0)
    cost = models.FloatField(verbose_name='Cost', default=0)

    def __str__(self):
        return self.color

    def update_remaining(self, qty_used):
        self.remaining -= qty_used
        return self.save()

    def remaining_percentage(self):
        per = round(self.remaining * 100 / 100, 2)
        return per

    class Meta:
        verbose_name = 'Silk'
        verbose_name_plural = 'Silks'


class Decorations(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    remaining = models.IntegerField(verbose_name='Remaining', default=0)
    cost = models.FloatField(verbose_name='Cost', default=0)
    price = models.FloatField(verbose_name='Price', default=0)

    def __str__(self):
        return self.name

    def update_remaining(self, qty_used):
        self.remaining -= qty_used
        return self.save()

    def remaining_percentage_dec(self):
        per = round(self.remaining * 100 / 50, 2)
        return per

    class Meta:
        verbose_name = 'Decoration'
        verbose_name_plural = 'Decorations'


class Materials(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    remaining = models.IntegerField(verbose_name='Remaining', default=0)
    cost = models.FloatField(verbose_name='Cost', default=0)
    price = models.FloatField(verbose_name='Price', default=0)

    def __str__(self):
        return self.name

    def update_remaining(self, qty):
        self.remaining -= qty
        self.save()

    def remaining_percentage_mat(self):
        per = round(self.remaining * 100 / 100, 2)
        return per

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'


class Product(models.Model):
    color = models.ForeignKey('Silk', on_delete=models.SET_NULL, null=True, blank=True)
    materials_id = models.ForeignKey('Materials', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField(verbose_name='Price', default=0)

    def cost(self):
        if self.materials_id and self.color:
            return round(self.materials_id.cost + self.color.cost * 1.60, 2)
        return 0

    def __str__(self):
        return f'{self.color} {self.materials_id} {self.cost()}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Order(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True)
    wrapping_paper = models.ForeignKey('Materials', on_delete=models.SET_NULL, null=True, blank=True, related_name='wrapping_paper')
    wrapping_paper_qty = models.IntegerField(verbose_name='Wrapping Paper Quantity', default=0, blank=True, null=True)

    def total(self):
        total_paper_price = self.wrapping_paper.price * self.wrapping_paper_qty if self.wrapping_paper and self.wrapping_paper_qty else 0

        order_line = self.orderline_set.all()
        total_product_price = sum(item.product.price * item.qty for item in order_line)

        dec_line = self.decorationline_set.all()
        total_decoration_price = sum(dec.decorations.price * dec.dec_qty for dec in dec_line)

        return round(total_product_price + total_decoration_price + total_paper_price, 2)

    total.short_description = 'Total'

    def expenses(self):
        total_paper_cost = self.wrapping_paper.cost * self.wrapping_paper_qty if self.wrapping_paper and self.wrapping_paper_qty else 0

        order_line = self.orderline_set.all()
        total_product_cost = sum(item.product.cost() * item.qty for item in order_line)

        dec_line = self.decorationline_set.all()
        total_decoration_cost = sum(dec.decorations.cost * dec.dec_qty for dec in dec_line)

        return round(total_product_cost + total_decoration_cost + total_paper_cost, 2)

    def profit(self):
        return round(self.total() - self.expenses(), 2)

    def adjust_inventory(self, adjust_by):
        if self.wrapping_paper:
            self.wrapping_paper.remaining += adjust_by * self.wrapping_paper_qty
            self.wrapping_paper.save()

        for line in self.orderline_set.all():
            line.product.materials_id.remaining += adjust_by * line.qty
            line.product.materials_id.save()

        for dec_line in self.decorationline_set.all():
            dec_line.decorations.remaining += adjust_by * dec_line.dec_qty
            dec_line.decorations.save()

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_order = Order.objects.get(pk=self.pk)
            old_order.adjust_inventory(1)  # Revert inventory changes from the old order
        super().save(*args, **kwargs)
        self.adjust_inventory(-1)  # Apply inventory changes from the new/updated order

    def delete(self, *args, **kwargs):
        self.adjust_inventory(1)  # Revert inventory changes before deleting
        super().delete(*args, **kwargs)

    def __str__(self):
        return f'{self.client}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderLine(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    qty = models.FloatField(verbose_name='Quantity', default=0)

    def __str__(self):
        return f'{self.qty} x {self.product} in Order #{self.order.id}'

    class Meta:
        verbose_name = 'Order Line'
        verbose_name_plural = 'Order Lines'


class DecorationLine(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True)
    decorations = models.ForeignKey('Decorations', on_delete=models.CASCADE, null=True)
    dec_qty = models.IntegerField(verbose_name='Decorations Quantity', default=0)

    class Meta:
        verbose_name = 'Decoration Line'
        verbose_name_plural = 'Decoration Lines'


class WrappingPaper(models.Model):
    use_wrapping_paper = models.BooleanField('Use Wrapping Paper', default=False)
    wrapping_paper = models.ForeignKey('Materials', on_delete=models.CASCADE, null=True, blank=True)
    paper_qty = models.IntegerField(verbose_name='Wrapping Paper Quantity', default=0, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.use_wrapping_paper:
            self.wrapping_paper = None
            self.paper_qty = 0
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Wrapping Paper'
        verbose_name_plural = 'Wrapping Papers'


class Client(models.Model):
    first_name = models.CharField(verbose_name='First name', max_length=50)
    last_name = models.CharField(verbose_name='Last name', max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
