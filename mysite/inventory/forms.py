from django import forms
from .models import Silk, Decorations, Materials, Order, OrderLine, DecorationLine, Client, Product


class SilkForm(forms.ModelForm):
    class Meta:
        model = Silk
        fields = ['color', 'remaining', 'cost']


class DecorationsForm(forms.ModelForm):
    class Meta:
        model = Decorations
        fields = ['name', 'remaining', 'cost', 'price']


class MaterialsForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = ['name', 'remaining', 'cost', 'price']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['wrapping_paper', 'wrapping_paper_qty']
        widgets = {
            'wrapping_paper': forms.Select(attrs={'class': 'form-control'}),
            'wrapping_paper_qty': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class OrderLineForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = OrderLine
        fields = ['product', 'qty']
        widgets = {
            'qty': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class DecorationLineForm(forms.ModelForm):
    decorations = forms.ModelChoiceField(queryset=Decorations.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = DecorationLine
        fields = ['decorations', 'dec_qty']
        widgets = {
            'dec_qty': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ProductForm(forms.ModelForm):
    color = forms.ModelChoiceField(queryset=Silk.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    materials_id = forms.ModelChoiceField(queryset=Materials.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['color', 'materials_id', 'price']
        widgets = {
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }


