from django.shortcuts import render
from django.http import HttpResponse
from perfil.models import Categoria
# Create your views here.

def definir_contas(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        return render(request, 'definir_contas.html', {'categorias': categorias})