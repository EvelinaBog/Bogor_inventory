from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inventory/', views.inventory, name='inventory'),
    path('edit/silk/<int:silk_id>/', views.edit_silk, name='edit-silk'),
    path('edit/decoration/<int:decoration_id>/', views.edit_decoration, name='edit-decoration'),
    path('edit/material/<int:material_id>/', views.edit_material, name='edit-material'),
    path('create/silk/', views.create_silk, name='create-silk'),
    path('create/decoration/', views.create_decoration, name='create-decoration'),
    path('create/material/', views.create_material, name='create-material'),
    path('orders/', views.orders, name='orders'),
    path('add_order/', views.add_order, name='add_order'),
    path('edit_order/<int:order_id>/', views.edit_order, name='edit_order'),
]
