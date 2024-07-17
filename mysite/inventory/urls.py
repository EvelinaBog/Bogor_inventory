from django.urls import path
from . import views
from .views import update_order_status

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
    path('orders/delete/<int:order_id>/', views.delete_order, name='delete_order'),
    path('add_order/', views.add_order, name='add_order'),
    path('edit_order/<int:order_id>/', views.edit_order, name='edit_order'),
    path('products/', views.create_product, name='create_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('silk/delete/<int:silk_id>/', views.delete_silk, name='delete-silk'),
    path('decoration/delete/<int:decoration_id>/', views.delete_decoration, name='delete-decoration'),
    path('material/delete/<int:material_id>/', views.delete_material, name='delete-material'),
    path('update_order_status/<int:order_id>/<str:status>/', update_order_status, name='update_order_status'),
]
