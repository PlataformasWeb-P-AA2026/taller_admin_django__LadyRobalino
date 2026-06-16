from django.db import models


class Museo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ciudad = models.CharField(max_length=100)
    anio_fundacion = models.IntegerField()

    def __str__(self):
        return self.nombre
    
    def costo_total_produccion(self):
        return sum(exhibicion.costo_produccion for exhibicion in self.exhibicion_set.all())

    def guia_con_mas_experiencia(self):
        return self.guia_museo_set.order_by('-anios_experiencia_guia').first()


class GuiaMuseo(models.Model):
    nombre_completo = models.CharField(max_length=100)
    anios_experiencia_guia = models.IntegerField()
    idiomas_hablados = models.CharField(max_length=200)
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_completo


class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField(max_length=100)
    duracion_meses = models.IntegerField()
    costo_produccion = models.DecimalField(max_digits=10, decimal_places=2)
    tematica = models.CharField(max_length=100)
    guia_museo = models.ForeignKey(GuiaMuseo, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo_exhibicion