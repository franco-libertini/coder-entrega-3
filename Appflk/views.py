from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.utils import timezone

# Create your views here.


def home(request):
    return render(request, 'index.html')

def autores(request):
    autores = Autor.objects.all()
    return render(request, 'autores.html', {
        'autores': autores,
    })

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {
        'categorias': categorias,
    })

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros.html', {
        'libros': libros
    })

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {
        'clientes': clientes
    })

def pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos.html', {
        'pedidos': pedidos
    })

#-- Formularios --#

def autoresForm(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            autor_nombre = form.cleaned_data.get('nombre')
            autor_biografia = form.cleaned_data.get('biografia')
            autor = Autor(nombre=autor_nombre, biografia=autor_biografia)
            autor.save()
            return redirect('autores')
    else:
        form = AutorForm()
        
    return render(request, 'autoresForm.html', {
        'form': form
    })
            
def categoriasForm(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria_nombre = form.cleaned_data.get('nombre')
            categoria = Categoria(nombre=categoria_nombre)
            categoria.save()
            return redirect('categorias')
    else:
        form = CategoriaForm()
        
    return render(request, 'categoriasForm.html', {
        'form': form
    })
    
def librosForm(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            
            libro = Libro(
                titulo = form.cleaned_data.get('titulo'),
                autor = form.cleaned_data.get('autor'),
                descripcion = form.cleaned_data.get('descripcion'),
                precio = form.cleaned_data.get('precio'),
                stock = form.cleaned_data.get('stock'),
                disponible = form.cleaned_data.get('disponible')
            )
            libro.save()
            
            categorias_ids = form.cleaned_data.get('categorias')
            libro.categorias.set(categorias_ids)
            
            return redirect('libros')
    else:
        form = LibroForm()
        
    autores = Autor.objects.all()
    categorias = Categoria.objects.all()
    
            
    return render(request, 'librosForm.html', {
        'form': form,
        'autores': autores,
        'categorias': categorias,
    })
    
def clientesForm(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = Cliente(
                nombre = form.cleaned_data.get('nombre'),
                apellido = form.cleaned_data.get('apellido'),
                email = form.cleaned_data.get('email'),
            )
            cliente.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
        
    return render(request, 'clientesForm.html', {
        'form': form
    })
    
def pedidosForm(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = Pedido(
                libro = form.cleaned_data.get('libro'),
                cliente = form.cleaned_data.get('cliente'),
                cantidad = form.cleaned_data.get('cantidad'),
            )
            pedido.save()
            return redirect('pedidos')
    else:
        form = PedidoForm()
        
    libros = Libro.objects.all()
    clientes = Cliente.objects.all()
        
    return render(request, 'pedidosForm.html', {
        'form': form,
        'libros': libros,
        'clientes': clientes
    })
    
#-- Buscadores --#

def buscar(request):
    return render(request, 'buscar.html')

def encontrarLibro(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        libros = Libro.objects.filter(titulo__icontains=patron)
        return render(request, 'libros.html', {
            'libros': libros
        })
        
    return render(request, 'libros.html', {
        'libros':  Libro.objects.all()
    })
    
def encontrarAutor(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        autores = Autor.objects.filter(nombre__icontains=patron)
        return render(request, 'autores.html', {
            'autores': autores
        })
        
    return render(request, 'autores.html', {
        'autores':  Autor.objects.all()
    })
    
def encontrarCategoria(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        categorias = Categoria.objects.filter(nombre__icontains=patron)
        return render(request, 'categorias.html', {
            'categorias': categorias
        })
        
    return render(request, 'categorias.html', {
        'categorias':  Categoria.objects.all()
    })
    
def encontrarCliente(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        clientes = Cliente.objects.filter(nombre__icontains=patron)
        return render(request, 'clientes.html', {
            'clientes': clientes
        })
        
    return render(request, 'clientes.html', {
        'clientes':  Cliente.objects.all()
    })
    
def encontrarPedido(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        pedidos = Pedido.objects.filter(cliente__nombre__icontains=patron)
        return render(request, 'pedidos.html', {
            'pedidos': pedidos
        })
        
    return render(request, 'pedidos.html', {
        'pedidos':  Pedido.objects.all()
    })