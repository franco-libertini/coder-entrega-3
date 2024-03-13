from django.urls import path
from .views import *

urlpatterns = [
    # Index
    path('', home, name='home'),
    # Modelos
    path('autores/', autores, name='autores'),
    path('categorias/', categorias, name='categorias'),
    path('libros/', libros, name='libros'),
    path('clientes/', clientes, name='clientes'),
    path('pedidos/', pedidos, name='pedidos'),
    # Formularios
    path('autor_form/', autoresForm, name='autor_form'),
    path('categoria_form/', categoriasForm, name='categoria_form'),
    path('libro_form/', librosForm, name='libro_form'),
    path('cliente_form/', clientesForm, name='cliente_form'),
    path('pedido_form/', pedidosForm, name='pedido_form'),
    # Busqueda
    path('buscar/', buscar, name='buscar'),
    path('encontrar_libro/', encontrarLibro, name='encontrar_libro'),
    path('encontrar_autor/', encontrarAutor, name='encontrar_autor'),
    path('encontrar_categoria/', encontrarCategoria, name='encontrar_categoria'),
    path('encontrar_cliente/', encontrarCliente, name='encontrar_cliente'),
    path('encontrar_pedido/', encontrarPedido, name='encontrar_pedido'),
]