from django.db import models

estadosInmueble = [
    ('Activo','Activo'),('Inactivo','Inactivo'),    
]

tiposInmueble = [
    ('Casa','Casa'),
    ('Apartamento','Apartamento'),  
    ('Local','Local'),  
    ('Oficina','Oficina'),  
    ('Bodega','Bodega'),  
    ('Lote','Lote'),  
    ('Finca','Finca'),  
]

class Usuario(models.Model):
    usuarioRol = models.CharField(max_length=50)
    usuarioLogin = models.CharField( max_length=50)
    usuarioPassword = models.CharField( max_length=50)
    usuarioEstado =models.CharField(max_length=50, null=False)
    
class Inmueble(models.Model):
    tipoInmueble = models.CharField( max_length=50, choices=tiposInmueble)
    nombreInmueble = models.CharField( max_length=100)
    descripcionInmueble = models.CharField( max_length=300)
    precioInmueble = models.IntegerField()
    direccionInmueble = models.CharField(max_length=50)
    estadoInmueble = models.CharField(max_length=50, choices=estadosInmueble,default="Activo")
    imagenInmueble = models.FileField(upload_to="Fotos/", null=True, blank=True)
    fechaInmueble = models.DateTimeField()
    
class Propietario(models.Model):
    nombrePropietario = models.CharField(max_length=50, null=False)
    telefonoPropietario = models.IntegerField()
    correoPropietario = models.CharField(max_length=100, null=False)
    fechaAgregacion = models.DateTimeField()
    
class Solicitud(models.Model):
    nombreCliente = models.CharField(max_length=50, null=False)
    telefonoCliente = models.IntegerField()
    correoCliente = models.CharField(max_length=100, null=False) 
    descripcionCliente = models.CharField(max_length=50, null=False)
    estadoCliente = models.CharField(max_length=50, null=False)
    fechaSolicitud = models.CharField(max_length=50, null=False)
    
class Roles(models.Model):
    rolNombre = models.CharField(max_length=50, null=False)
    estadoRol = models.CharField(max_length=50, null=False)
    


