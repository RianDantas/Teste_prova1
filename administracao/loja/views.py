from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

# Create your views here.

def cadastrar(request):
    produto = Produto.objects.get(id=2)
    return HttpResponse(produto)

