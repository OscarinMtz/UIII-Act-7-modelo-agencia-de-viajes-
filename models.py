from django.db import models

class Destino(models.Model):
    id_destino = models.AutoField(primary_key=True)
    nombre_destino = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    continente = models.CharField(max_length=50)
    descripcion = models.TextField()
    atracciones_principales = models.TextField()
    clima = models.CharField(max_length=50)
    divisa_local = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_destino

class AgenteViajes(models.Model):
    id_agente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    dni = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    comision_porcentaje = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class ClienteViajes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    fecha_registro = models.DateField()
    preferencias_viaje = models.TextField()
    pasaporte = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Vuelo(models.Model):
    id_vuelo = models.AutoField(primary_key=True)
    num_vuelo = models.CharField(max_length=20)
    aerolinea = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha_salida = models.DateField()
    hora_salida = models.TimeField()
    fecha_llegada = models.DateField()
    hora_llegada = models.TimeField()
    precio_clase_economica = models.DecimalField(max_digits=10, decimal_places=2)
    asientos_disponibles = models.IntegerField()

    def __str__(self):
        return f"{self.num_vuelo} - {self.aerolinea}"

class Alojamiento(models.Model):
    id_alojamiento = models.AutoField(primary_key=True)
    nombre_hotel = models.CharField(max_length=255)
    tipo_alojamiento = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    estrellas = models.IntegerField()
    precio_noche_estandar = models.DecimalField(max_digits=10, decimal_places=2)
    servicios_incluidos = models.TextField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_hotel

class PaqueteTuristico(models.Model):
    id_paquete = models.AutoField(primary_key=True)
    nombre_paquete = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    id_destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    precio_adulto = models.DecimalField(max_digits=10, decimal_places=2)
    precio_nino = models.DecimalField(max_digits=10, decimal_places=2)
    cupo_maximo = models.IntegerField()
    incluye_vuelo = models.BooleanField()
    incluye_alojamiento = models.BooleanField()

    def __str__(self):
        return self.nombre_paquete

class ReservaViaje(models.Model):
    ESTADOS_RESERVA = [
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada'),
        ('PAGADA', 'Pagada'),
    ]
    
    id_reserva = models.AutoField(primary_key=True)
    id_paquete = models.ForeignKey(PaqueteTuristico, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(ClienteViajes, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField()
    num_adultos = models.IntegerField()
    num_ninos = models.IntegerField()
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    estado_reserva = models.CharField(max_length=50, choices=ESTADOS_RESERVA)
    fecha_vencimiento_pago = models.DateField()
    id_agente_venta = models.ForeignKey(AgenteViajes, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva {self.id_reserva} - {self.id_cliente}"
