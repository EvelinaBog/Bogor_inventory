from django.shortcuts import render, redirect, get_object_or_404
from .models import Silk, Decorations, Materials, Order
from .forms import SilkForm, DecorationsForm, MaterialsForm


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
