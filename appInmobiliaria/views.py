from django.shortcuts import render,redirect
from appInmobiliaria.models import *
from django.db import Error, transaction
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from smtplib import SMTPException
import threading
import urllib

def inicio(request):
    return render(request,"inicio.html")

def listarInmuebles(request):
    mensaje = ""
    estado = False
    try:
        inmuebles = Inmueble.objects.all()
        estado = True
    except Error as error:
        mensaje = f"Problemas al obtener los inmuebles {error}"
        
    retorno = {"mensaje":mensaje,"esatdo":estado,"listaInmuebles":inmuebles}
    return render(request,"inmuebles.html",retorno)
    # inmuebles = Inmueble.objects.all()
    # retorno = {"inmuebles": inmuebles}
    # print(retorno)
    # return render(request,"inmuebles.html")

def contactenos(request):
    return render(request,"contactenos.html")

def vistaInmueble(request,id_inmueble):
    Inmueble.save
    return render(request,"vistaInmueble.html")

def agregarInmueble(request):
    inmueble = Inmueble.objects.all()
    retorno = {"tiposInmueble":tiposInmueble}
    return render(request,"agregarInmueble.html",retorno)

def agregarInmuebleDatos(request, method='POST'):
    if request.method == 'POST':
        estado = False
        mensaje = f""
        try:
            with transaction.atomic():
                nombre = request.POST['txtnombreInmueble']
                tipoInmueble = request.POST['txtTipoInmueble']
                descripcion = request.POST['txtDescripcionInmueble']
                precio = request.POST['txtPrecioInmueble']
                direccion = request.POST['txtDireccion']
                imagen = request.POST['txtImagen']
                fecha = request.POST['txtFecha']
                inmueble = Inmueble(tipoInmueble=tipoInmueble,descripcionInmueble=descripcion,
                        precioInmueble=precio,
                        direccionInmueble=direccion,
                        imagenInmueble=imagen,nombreInmueble= nombre,fechaInmueble= fecha)
                inmueble.save()
        except Error as error:
            transaction.rollback()
    

    return render(request,"inicio.html")

def agregarPersona(request):
    return render(request,"agregarPersona.html")

def vistaAgregarPropietario(request):
    return render(request,"agregarPropietario.html")

def agregarPropietarioDatos(request, method='POST'):
     if request.method == 'POST':
        estado = False
        mensaje = f""
        try:
            nombre = request.POST['txtNombre']
            correo = request.POST['txtCorreo']
            telefono = request.POST['txtTelefono']
            fecha = request.POST['txtFecha']
            propietario= Propietario(nombrePropietario=nombre,telefonoPropietario=telefono,
                                     correoPropietario=correo, fechaAgregacion=fecha,
                                    )
            propietario.save()
        except Error as error:
            transaction.rollback()
        return render(request, "inicio.html")

def consultarInmueble (request):
    mensaje= ""
    inmuebles= None 
    try:
        inmuebles=list(Inmueble.objects.all)
    except:
        mensaje="No existe este Inmueble"
    retorno = {"inmuebles":Inmueble,"mensaje":mensaje,}
    return render(request,"vistaInmueble.html",retorno)
        
def iniciarSesion(request):
    mensaje=""
    categorias=None
    producto=None
    try:
        inmueble = Inmueble.objects.all()
    except:
        mensaje="No existe Producto"
    retorno = {"Inmueble":Inmueble, "mensaje":mensaje}
    return render(request,"inmuebles.html",retorno)
    
def inicioPagina(request):
    return render(request,"inicioPagina.html")

def iniciarSesion(request):
    usernames = request.POST['txtLogin']   
    password = request.POST['txtPassword']
    user = authenticate(username=usernames, password=password)
    if user is not None:
        auth.login(request, user)
        if user.is_superuser:
            return redirect('/admin/')
        else:
            return render(request,'agregarInmueble.html')
    else:
        return render(request,'agregarInmueble.html')
    return render(request, 'agregarInmueble.html')
    
    
def cerrarSesion(request):
    auth.logout(request)
    return redirect('../login')

def inicioPagina(request):
    return render(request,"inicioPagina.html")

def login(request):
    return render(request,"frmIniciarSesion.html")
