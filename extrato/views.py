from django.shortcuts import render, redirect
from perfil.models import Categoria, Conta

def novo_valor(request):
    if request.method == 'GET':
        contas = Conta.objects.all()
        return render(request, 'novo_valor.html')