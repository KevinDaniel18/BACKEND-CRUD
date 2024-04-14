from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

# Create your models here.
class Employee(models.Model):

    TIPO_IDENTIFICACION_CHOICES = [
        ('nit', 'NIT'),
        ('cc', 'Cédula de Ciudadanía'),
    ]

    PHONE_TYPE_CHOICES = [
        ('cell', 'Celular'),
        ('tel', 'Teléfono'),
    ]

    DEFAULT_TIPO_IDENTIFICACION = 'nit'
    DEFAULT_CARGO = ''
    DEFAULT_DEPARTAMENTO = ''
    DEFAULT_IDENTIFICACION = ''
    DEFAULT_SALARIO_MENSUAL = 0.00
    DEFAULT_PHONE_TYPE = 'cell'
    DEFAULT_NUMBER = ''
    DEFAULT_EMAIL = '' 

    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    tipo_identificacion = models.CharField(max_length=3, choices = TIPO_IDENTIFICACION_CHOICES, default=DEFAULT_TIPO_IDENTIFICACION)
    identificacion = models.CharField(max_length=20, default=DEFAULT_IDENTIFICACION) 
    fecha_ingreso = models.DateField(default=timezone.now)
    salario_mensual = models.DecimalField(max_digits=10, decimal_places=2, default=DEFAULT_SALARIO_MENSUAL) 
    cargo = models.CharField(max_length=100, default=DEFAULT_CARGO)
    departamento = models.CharField(max_length=100, default=DEFAULT_DEPARTAMENTO)
    type = models.CharField(max_length=4, choices=PHONE_TYPE_CHOICES, default=DEFAULT_PHONE_TYPE)
    number = models.CharField(max_length=15, default=DEFAULT_NUMBER) 
    email = models.EmailField(default=DEFAULT_EMAIL) 

    def __str__(self):
        return self.nombres

@receiver(post_save, sender=Employee)
def enviar_correo_cuando_email_lleno(sender, instance, created, **kwargs):
    if instance.email:  # Verificar si el campo email no está vacío
        if created:
            asunto = "Datos registrados correctamente"
            mensaje = f"Bienvenido/a {instance.nombres} {instance.apellidos}!\n\n" \
                      f"Tus datos fueron registrados correctamente.\n\n" \
                      f"Información:\n" \
                      f"- Cargo: {instance.cargo}\n" \
                      f"- Departamento: {instance.departamento}\n" \
                      f"- Salario Mensual: {instance.salario_mensual}\n\n" \
                      f"¡Gracias por tu registro!"
        else:
            asunto = "Datos modificados correctamente"
            mensaje = f"Hola {instance.nombres} {instance.apellidos}!\n\n" \
                      f"Tus datos fueron modificados correctamente.\n\n" \
                      f"Información actualizada:\n" \
                      f"- Cargo: {instance.cargo}\n" \
                      f"- Departamento: {instance.departamento}\n" \
                      f"- Salario Mensual: {instance.salario_mensual}\n\n" \
                      f"¡Gracias por tu actualización!"
        
        remitente = settings.EMAIL_HOST_USER  # Obtener el remitente de la configuración de Django
        destinatario = instance.email

        send_mail(asunto, mensaje, remitente, [destinatario])

@receiver(post_delete, sender=Employee)
def enviar_correo_cuando_empleado_borrado(sender, instance, **kwargs):
    if instance.email:  # Verificar si el campo email no está vacío
        asunto = "Datos borrados correctamente"
        mensaje = f"Hola! {instance.nombres} {instance.apellidos}, Tus datos han sido borrados correctamente."
        remitente = settings.EMAIL_HOST_USER  # Obtener el remitente de la configuración de Django
        destinatario = instance.email

        send_mail(asunto, mensaje, remitente, [destinatario])