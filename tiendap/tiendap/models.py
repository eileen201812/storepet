from django.db import models

class Contacto(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    run = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    dv = models.CharField(max_length=1, blank=True, null=True)
    nombres = models.CharField(max_length=80, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=80, blank=True, null=True)
    apellido_materno = models.CharField(max_length=80, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    telefono = models.CharField(max_length=16, blank=True, null=True)
    asunto = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacto'