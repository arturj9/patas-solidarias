from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def cadastro(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Olá estou no cadastro')