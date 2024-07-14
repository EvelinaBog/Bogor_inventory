from django.db import models

# Create your models here.


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
        return round(self.materials_id.cost + self.color.cost * 1.60, 2)

    cost.short_description = 'Cost'

    def __str__(self):
        return f'{self.color} {self.materials_id} {self.cost()}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Order(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    wrapping_paper = models.ForeignKey('Materials', on_delete=models.CASCADE, null=True)

    def total(self):
        wrapping_paper = self.wrappingpaper_set.all()
        total_paper_price = sum(paper.wrapping_paper.price * paper.paper_qty for paper in wrapping_paper)
        order_line = self.orderline_set.all()
        total_product_price = sum(item.product.price * item.qty for item in order_line)
        dec_line = self.decorationline_set.all()
        total_decoration_price = sum(dec.decorations.price * dec.dec_qty for dec in dec_line)
        return round(total_product_price + total_decoration_price + total_paper_price, 2)

    total.short_description = 'Total'

    def expenses(self):
        wrapping_paper = self.wrappingpaper_set.all()
        total_paper_cost = sum(paper.wrapping_paper.cost * paper.paper_qty for paper in wrapping_paper)
        order_line = self.orderline_set.all()
        total_product_cost = sum(item.product.cost() * item.qty for item in order_line)
        dec_line = self.decorationline_set.all()
        total_decoration_cost = sum(dec.decorations.cost * dec.dec_qty for dec in dec_line)
        return round(total_product_cost + total_decoration_cost + total_paper_cost, 2)

    def profit(self):
        return self.total() - self.expenses()

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
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True)
    wrapping_paper = models.ForeignKey('Materials', on_delete=models.CASCADE, null=True)
    paper_qty = models.IntegerField(verbose_name='Wrapping paper quantity', default=0)

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

