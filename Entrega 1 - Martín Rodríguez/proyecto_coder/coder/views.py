
from django.shortcuts import render

from http.client import HTTPResponse
from urllib.request import HTTPErrorProcessor
from django.shortcuts import render
from django.http import HttpResponse
from coder.models import Torneos, Escuelas, Reservas
from coder.forms import FormularioBusquedaTorneo, FormularioBusquedaReserva

def index(request):
    return render(request, "coder/index.html", {"mensaje": "Reservar tu cancha está a sólo unos clicks de distancia"}) #esto renderiza el template de una, sin loader ni plantillas.remder
