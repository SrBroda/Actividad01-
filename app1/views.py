from django.shortcuts import render


# app1/views.py
from django.shortcuts import render
from django.http import HttpResponse

def vista_uno(request):
    return HttpResponse("<h1>Wenas, esta es la vista 1 de la App 1</h1>")

def vista_dos(request):
    return HttpResponse("<h1>Wenas, esta es la vista 2 de la App 1</h1>")

