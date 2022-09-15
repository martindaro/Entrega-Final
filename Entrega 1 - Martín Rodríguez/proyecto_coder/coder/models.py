from django.db import models
class Torneos(models.Model):
    deporte = models.CharField(max_length=38)
    horario = models.CharField(max_length=38)
    sedes = models.CharField(max_length=38)
    categoría = models.CharField(max_length=38)

class Escuelas(models.Model): #exEstudiante
    deporte = models.CharField(max_length=38)
    horario = models.CharField(max_length=38)
    sedes = models.CharField(max_length=38)
    edad = models.IntegerField()

class Reservas(models.Model): #exProfesor
    nombre = models.CharField(max_length=38)
    apellido = models.CharField(max_length=38)
    email = models.EmailField()
    celular = models.IntegerField()
    fecha_reserva = models.DateField()

#def __str__(self):
    #return f"{self.nombre} - {self.apellido}"