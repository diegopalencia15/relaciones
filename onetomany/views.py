from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

# Create your views here.
def create(request):
    r = Reporter(first_name="John", last_name="Smith", email="john@example.com")
    r.save()

    r2 = Reporter(first_name="Paul", last_name="Jones", email="paul@example.com")
    r2.save()

    a = Article(id=None, headline="This is a test", pub_date=date(2005, 7, 27), reporter=r)
    a.save()

    a.reporter.id
    a.reporter

    return HttpResponse("Uno a muchos")

def  consultar (request, id):
  r = Reporter.objects.get(id=id) #trae el registro que coincida con la llave primaria

  print (r)
  return HttpResponse (f"Primer Nombre: {r.first_name}, Apellido: {r.last_name}, email: {r.email}")  

def  modificar(request,first_name,last_name,email,id):
    
  r = Reporter.objects.get(id=id)
  r.first_name = first_name
  r.last_name = last_name
  r.email = email
  r.save()
  

  return HttpResponse ('Se actualizaron los Datos')

def eliminar(request,id):
  r = Reporter.objects.get(id=id)
  r.delete()
  return HttpResponse ("Registro Eliminado")