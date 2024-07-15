from django.shortcuts import render, redirect, get_object_or_404
from .models import Silk, Decorations, Materials, Order, OrderLine, DecorationLine, Client, Product
from .forms import SilkForm, DecorationsForm, MaterialsForm, OrderForm, OrderLineForm, DecorationLineForm, ClientForm
from django.forms import inlineformset_factory


def index(request):
    try:
        silk_data = Silk.objects.all()
        silk_colors = [silk.color for silk in silk_data]
        silk_remainings = [silk.remaining for silk in silk_data]
        silk_data_zipped = zip(silk_colors, silk_remainings)
    except Silk.DoesNotExist:
        silk_data_zipped = []

    try:
        decorations_data = Decorations.objects.all()
        decoration_type = [decoration.name for decoration in decorations_data]
        decoration_remaining = [decoration.remaining for decoration in decorations_data]
        decoration_per = [decoration.remaining_percentage_dec() for decoration in decorations_data]
        decoration_data_zipped = zip(decoration_type, decoration_remaining)
    except Decorations.DoesNotExist:
        decoration_data_zipped = []
    try:
        materials_data = Materials.objects.all()
        materials_type = [materials.name for materials in materials_data]
        materials_remaining = [materials.remaining for materials in materials_data]
        materials_data_zipped = zip(materials_type, materials_remaining)
    except Materials.DoesNotExist:
        materials_data_zipped = []

    orders = Order.objects.all()
    total = sum(order.total() for order in orders)
    expenses = sum(order.expenses() for order in orders)
    profit = sum(order.profit() for order in orders)

    context = {
        'total': total,
        'expenses': expenses,
        'profit': profit,
        'silk_data_zipped': silk_data_zipped,
        'decoration_data_zipped': decoration_data_zipped,
        'materials_data_zipped': materials_data_zipped,
        'decoration_per': decoration_per,

    }

    return render(request, template_name='index.html', context=context)


def inventory(request):
    silks = Silk.objects.all()
    decorations = Decorations.objects.all()
    materials = Materials.objects.all()
    return render(request, 'inventory.html', {'silks': silks, 'decorations': decorations, 'materials': materials})


def edit_silk(request, silk_id):
    silk = get_object_or_404(Silk, id=silk_id)
    if request.method == 'POST':
        form = SilkForm(request.POST, instance=silk)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = SilkForm(instance=silk)
    return render(request, 'edit_silk.html', {'form': form})


def edit_decoration(request, decoration_id):
    decoration = get_object_or_404(Decorations, id=decoration_id)
    if request.method == 'POST':
        form = DecorationsForm(request.POST, instance=decoration)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = DecorationsForm(instance=decoration)
    return render(request, 'edit_decoration.html', {'form': form})


def edit_material(request, material_id):
    material = get_object_or_404(Materials, id=material_id)
    if request.method == 'POST':
        form = MaterialsForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = MaterialsForm(instance=material)
    return render(request, 'edit_material.html', {'form': form})


def create_silk(request):
    if request.method == 'POST':
        form = SilkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = SilkForm()
    return render(request, 'create_silk.html', {'form': form})


def create_decoration(request):
    if request.method == 'POST':
        form = DecorationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = DecorationsForm()
    return render(request, 'create_decoration.html', {'form': form})


def create_material(request):
    if request.method == 'POST':
        form = MaterialsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = MaterialsForm()
    return render(request, 'create_material.html', {'form': form})


def orders(request):
    order_list = Order.objects.all()
    return render(request, 'orders.html', {'orders': order_list})


def add_order_line(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderLineForm(request.POST)
        if form.is_valid():
            order_line = form.save(commit=False)
            order_line.order = order
            order_line.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderLineForm()
    return render(request, 'add_order_line.html', {'form': form, 'order': order})


def add_decoration_line(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = DecorationLineForm(request.POST)
        if form.is_valid():
            decoration_line = form.save(commit=False)
            decoration_line.order = order
            decoration_line.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = DecorationLineForm()
    return render(request, 'add_decoration_line.html', {'form': form, 'order': order})


def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    OrderLineFormSet = inlineformset_factory(Order, OrderLine, form=OrderLineForm, extra=0, can_delete=True)
    DecorationLineFormSet = inlineformset_factory(Order, DecorationLine, form=DecorationLineForm, extra=1, can_delete=True)

    if request.method == 'POST':
        order_form = OrderForm(request.POST, instance=order)
        order_line_formset = OrderLineFormSet(request.POST, instance=order)
        decoration_line_formset = DecorationLineFormSet(request.POST, instance=order)

        if order_form.is_valid() and order_line_formset.is_valid() and decoration_line_formset.is_valid():
            order_form.save()
            order_line_formset.save()
            decoration_line_formset.save()
            return redirect('orders')
    else:
        order_form = OrderForm(instance=order)
        order_line_formset = OrderLineFormSet(instance=order)
        decoration_line_formset = DecorationLineFormSet(instance=order)

    return render(request, 'edit_order.html', {
        'order_form': order_form,
        'formset': order_line_formset,
        'decoration_line_formset': decoration_line_formset,
    })

def add_order(request):
    DecorationLineFormSet = inlineformset_factory(Order, DecorationLine, form=DecorationLineForm, extra=1, can_delete=True)

    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        order_form = OrderForm(request.POST)
        order_line_form = OrderLineForm(request.POST)
        decoration_line_formset = DecorationLineFormSet(request.POST)

        if client_form.is_valid() and order_form.is_valid() and order_line_form.is_valid() and decoration_line_formset.is_valid():
            client = client_form.save()
            order = order_form.save(commit=False)
            order.client = client
            order.save()
            order_line = order_line_form.save(commit=False)
            order_line.order = order
            order_line.save()

            decoration_line_formset.instance = order
            decoration_line_formset.save()

            return redirect('orders')  # Replace with the name of your order list view
    else:
        client_form = ClientForm()
        order_form = OrderForm()
        order_line_form = OrderLineForm()
        decoration_line_formset = DecorationLineFormSet()

    return render(request, 'add_order.html', {
        'client_form': client_form,
        'order_form': order_form,
        'order_line_form': order_line_form,
        'decoration_line_formset': decoration_line_formset,
    })
