from django.shortcuts import render, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import statistics
from django.db.models import Avg

# Create your views here.
def index(request):
    pts = list(puntos.objects.values('id','lngLat','nombrePunto'))
    return render(request, "index.html", context={"puntos": pts})

def addPunto(request, lng, lat):
    if(request.method == "POST"):
        nombreP = request.POST["nombrePunto"]
        direccionP = request.POST["direccionPunto"]
        descP = request.POST["descripcionP"]
        pto = puntos.objects.create(nombrePunto = str(nombreP), direccionPunto = str(direccionP),descripcionPunto=str(descP), lngLat=lng+":"+lat)
        pto.save()
        return redirect("/index")
    return render(request,"addPto.html", context={"lng":float(lng),"lat":float(lat)})

def verPunto(request, idP):
    if(request.method == "POST"):
        com = request.POST["comentariosP"]
        val = request.POST["valoracion"]
        pto = puntos.objects.filter(id =idP)[0]
        c = comentarios.objects.create(idPunto = pto, valoracion = val, comentarios = com)
        c.save()
        return redirect("/verPunto/"+str(idP)+"/")
    punto = puntos.objects.filter(id=idP)[0]
    comments = comentarios.objects.filter(idPunto=punto.id)
    processC = list(comentarios.objects.filter(idPunto=punto.id))
    if(len(processC) != 0):
        med = int(comentarios.objects.filter(idPunto=punto.id).aggregate(Avg('valoracion'))["valoracion__avg"])
    else:
        med = 0
    return render(request,"verPto.html", context={"punto":punto, "comments":comments, "media":med, "lat":punto.lngLat.split(":")[1],"lng":punto.lngLat.split(":")[0]})

def delPunto(request, idP):
    puntos.objects.filter(id=idP).delete()
    return redirect('/index')
