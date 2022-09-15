from django.forms import Form, CharField, EmailField, IntegerField, DateField

#De búsqueda

class FormularioBusquedaTorneo(Form):
    nombre = CharField(max_length=38)
    apellido = CharField(max_length=38)
    deporte = CharField(max_length=38)
    email = EmailField()

class FormularioBusquedaEscuela(Form):
    nombre = CharField(max_length=38)
    apellido = CharField(max_length=38)
    deporte = CharField(max_length=38)
    email = EmailField()

class FormularioBusquedaReserva(Form):
    nombre = CharField(max_length=38)
    apellido = CharField(max_length=38)
    email = EmailField()
    celular = IntegerField()
    fecha_reserva = DateField()
