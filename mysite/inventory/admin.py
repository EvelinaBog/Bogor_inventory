from django.contrib import admin
from .models import Silk, Decorations, Materials, Product, Order, OrderLine, Client, DecorationLine, WrappingPaper
# Register your models here.


class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'get_total', 'get_profit', 'get_expenses')
    inlines = [OrderLineInline]
    readonly_fields = ('get_total',)

    def get_total(self, obj):
        return obj.total()
    get_total.short_description = 'Total'

    def get_profit(self, obj):
        return obj.profit()
    get_profit.short_description = 'Profit'

    def get_expenses(self, obj):
        return obj.expenses()
    get_expenses.short_description = 'Expenses'


class SilkAdmin(admin.ModelAdmin):
    list_display = ('color', 'remaining', 'cost', 'get_remaining_percentage')

    def get_silk_remaining(self, obj):
        return obj.get_silk_remaining()
    get_silk_remaining.short_description = 'Silk Remaining'

    def get_remaining_percentage(self, obj):
        return obj.remaining_percentage()
    get_remaining_percentage.short_description = 'Percentages'


class DecorationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'remaining', 'cost', 'price')

    def get_decorations_remaining(self, obj):
        return obj.decorations_remaining()
    get_decorations_remaining.short_description = 'Decorations Remaining'

    def get_remaining_percentage_dec(self, obj):
        return obj.remaining_percentage_dec()
    get_remaining_percentage_dec.short_description = 'Decorations Percentages'


class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'remaining', 'cost')

    def get_remaining_percentage_mat(self, obj):
        return obj.remaining_percentage_mat()
    get_remaining_percentage_mat.short_description = 'Materials Percentages'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('color', 'materials_id', 'price', 'get_cost',)

    def get_cost(self, obj):
        return obj.cost()
    get_cost.short_description = 'Cost'

    def get_remaining(self, obj):
        return obj.remaining()
    get_remaining.short_description = 'Remaining'


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'qty')


class DecorationLineAdmin(admin.ModelAdmin):
    list_display = ('order', 'decorations', 'dec_qty')

    def get_remaining(self, obj):
        return obj.decorations.decorations_remaining()
    get_remaining.short_description = 'Decorations Remaining'



admin.site.register(Silk, SilkAdmin)
admin.site.register(Decorations, DecorationsAdmin)
admin.site.register(Materials, MaterialsAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
admin.site.register(Client)
admin.site.register(DecorationLine, DecorationLineAdmin)
admin.site.register(WrappingPaper)
