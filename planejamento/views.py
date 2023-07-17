from django.shortcuts import render, redirect
from perfil.models import Categoria
from django.http import HttpResponse

# Create your views here.
def definir_planejamento(request):
  categorias = Categoria.objects.all()
  return render(request, 'definir_planejamento.html', {'categorias': categorias})
  