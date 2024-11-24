from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Proveedor, Producto


# Create your views here.

def proveedor(request):
    provedor = Proveedor.objects.all()
    return render(request, "proveedor.html" ,{
        "proveedor" : provedor
    })


def productos(request):
    producto = Producto.objects.all()
    return render(request,'productos.html', {
        "producto":producto
    })


def create_proveedor(request):
    if request.method == 'GET':  
        return render(request, 'create_proveedor.html')  
    elif request.method == 'POST':  
        nombre = request.POST.get('txtNombre', '').strip()
        direccion = request.POST.get('txtdireccion', '').strip()
        telefono = request.POST.get('txtfono', '').strip()
        email = request.POST.get('txtemail', '').strip()

        
        if not nombre or not direccion or not telefono or not email:
            return render(request, 'create_proveedor.html', {
                'error': 'Todos los campos son obligatorios.'
            })

        
        Proveedor.objects.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            email=email
        )
        return redirect('proveedor')  


def create_producto(request):
    if request.method == 'GET':
        
        proveedores = Proveedor.objects.all()
        return render(request, 'create_producto.html', {'proveedores': proveedores})
    elif request.method == 'POST':
        
        nombre = request.POST['txtProducto']
        descripcion = request.POST['txtdescripcion']
        precio = request.POST['txtprecio']
        stock = request.POST['txtstock']
        provedor_id = request.POST['selectProveedor']

        
        provedor = Proveedor.objects.get(id=provedor_id)

       
        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            provedor=provedor,
        )

        return redirect('productos')



def editarProveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)  

    if request.method == 'POST':  
        nombre = request.POST.get('txtNombre', '').strip()
        direccion = request.POST.get('txtdireccion', '').strip()
        telefono = request.POST.get('txtfono', '').strip()
        email = request.POST.get('txtemail', '').strip()

        
        proveedor.nombre = nombre
        proveedor.direccion = direccion
        proveedor.telefono = telefono
        proveedor.email = email
        proveedor.save()

        return redirect('proveedor')  

    
    return render(request, 'editarProveedor.html', {
        'proveedor': proveedor
    })


def editarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)  

    if request.method == 'POST':  
        nombre = request.POST.get('txtProducto')
        descripcion = request.POST.get('txtdescripcion')
        precio = request.POST.get('txtprecio')
        stock = request.POST.get('txtstock')

        
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio
        producto.stock = stock
        producto.save()

        return redirect('productos')  

    
    return render(request, 'editarProducto.html', {
        'producto': producto
    })

    


def eliminarProveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()

    return redirect('proveedor')

def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('productos')
