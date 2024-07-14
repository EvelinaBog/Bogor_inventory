# forms.py

from django import forms
from .models import Silk, Decorations, Materials


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
