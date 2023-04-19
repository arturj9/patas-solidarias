from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def cadastro(request: HttpRequest) -> render:
    if request.method == 'GET':
        return render(request, 'cadastro.html')