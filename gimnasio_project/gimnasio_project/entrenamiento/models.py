from django.db import models

class Gimnasio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    numero_max_socios = models.IntegerField()
    numero_contacto = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} - {self.ciudad}"

class PlanEntrenamiento(models.Model):
    nombre = models.CharField(max_length=100)  # Ej: musculación
    duracion_semanas = models.IntegerField()
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    gimnasio = models.ForeignKey(Gimnasio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.duracion_semanas} semanas)"