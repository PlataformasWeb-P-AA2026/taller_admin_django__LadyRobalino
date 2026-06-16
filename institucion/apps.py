from django.apps import AppConfig

from institucion import models


class InstitucionConfig(AppConfig):
    name = 'institucion'

# Clase museo con atributos: nombre: Nombre del museo (cadena de texto, único, no nulo).
#ciudad: Ciudad donde se ubica el museo (cadena de texto).
#año_fundacion: Año de fundación del museo (número entero).

class Museo(models.Model):
    nombre = models.CharField(max_length=100, unique=True, null=False)
    ciudad = models.CharField(max_length=100)
    anio_fundacion = models.IntegerField()

    def __str__(self):
        return self.nombre
    

#clase Guia_museo con estos atributos: Atributos:
#nombre_completo: Nombres y apellidos completos del guía (cadena de texto).
#años_experiencia_guia: Años de experiencia como guía de museo (número entero).
#idiomas_hablados: Idiomas que el guía puede hablar (ej: "Español, Inglés") (cadena de texto).
#Relación: un guía de museo trabaja en un museo)

class GuiaMuseo(models.Model):
    nombre_completo = models.CharField(max_length=100)
    anios_experiencia_guia = models.IntegerField()
    idiomas_hablados = models.CharField(max_length=200)
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE)

    def __str__(sefl):
        return self.nombre_completo
    

# clase Exhibicion con atrinutos: 
# titulo_exhibicion: Título de la exhibición (cadena de texto).
#duracion_meses: Duración de la exhibición en meses (número entero).
#costo_produccion: Costo total de producción de la exhibición (número decimal).
#tematica: Temática principal de la exhibición (cadena de texto).
#Relación: una exhibición es asistida por un guía de museo

class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField(max_length=100)
    duracion_meses = models.IntegerField()
    costo_produccion = models.DecimalField(max_digits=10, decimal_places=2)
    tematica = models.CharField(max_length=100)
    guia_museo = models.ForeignKey(GuiaMuseo, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo_exhibicion
    