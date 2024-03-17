from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant
from datetime import date

# Create your views here.
def create(request):
    p1 = Place(name="Demon Dogs", address="944 W. Fullerton")
    p1.save()
    p2 = Place(name="Ace Hardware", address="1013 N. Ashland")
    p2.save()

    r = Restaurant(place=p1, employes=25)
    r.save()

    # restaurante = Restaurant.objects.get(place_id=3)
    # print(restaurante.place.address)

    return HttpResponse("datos creados uno a uno")

def  consultar (request, id):
  r = Place.objects.get(id=id) #trae el registro que coincida con la llave primaria

  print (r)
  return HttpResponse (f"Nombre: {r.name}, Direccion: {r.address}")  

def  modificar(request,name,address,id):
    
  r = Place.objects.get(id=id)
  r.name = name
  r.address = address
  r.save()
  

  return HttpResponse ('Se actualizaron los Datos')

def eliminar(request,id):
  r = Place.objects.get(id=id)
  r.delete()
  return HttpResponse ("Registro Eliminado")