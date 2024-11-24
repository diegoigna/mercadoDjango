from django.urls import path
from .import views

urlpatterns = [
    path('', views.proveedor, name='proveedor'),
    path('productos/', views.productos, name="productos"),
    path('create_proveedor/', views.create_proveedor, name="create_proveedor"),
    path('create_producto/', views.create_producto, name="create_producto"),
    path('editarProducto/<int:id>', views.editarProducto, name='editarProducto'),
    path('editarProveedor/<int:id>', views.editarProveedor, name='editarProveedor'),
    path('productos/eliminarProducto/<id>', views.eliminarProducto),
    path('eliminarProveedor/<id>', views.eliminarProveedor ),
]