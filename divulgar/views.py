from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Tag, Raca

@login_required
def novo_pet(request:HttpRequest) -> render:
    if request.method ==  'GET':
        tags = Tag.objects.all()
        return render(request, 'novo_pet.html', {'tags': tags})
    elif request.method == 'POST':
        ...