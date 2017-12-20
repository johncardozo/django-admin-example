from django.db import models

class Autor(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    celular = models.CharField(max_length=200, null=True, blank=True)
    documento = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

    class Meta:
        verbose_name = u'Autor'
        verbose_name_plural = u'Autores'


class Asesor(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    celular = models.CharField(max_length=200, null=True, blank=True)
    documento = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

    class Meta:
        verbose_name = u'Asesor'
        verbose_name_plural = u'Asesores'


class Par(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    celular = models.CharField(max_length=200, null=True, blank=True)
    documento = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

    class Meta:
        verbose_name = u'Par'
        verbose_name_plural = u'Pares'


class Modulo(models.Model):
    nombre = models.CharField(max_length=200)
    porcentaje_avance = models.IntegerField(default=0, null=True, blank=True)
    
    autor = models.ForeignKey(Autor, related_name="modulos", on_delete=models.PROTECT, null=True, blank=True)
    asesor = models.ForeignKey(Asesor, related_name="modulos", on_delete=models.PROTECT, null=True, blank=True)
    par = models.ForeignKey(Par, related_name="modulos", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = u'Módulo'
        verbose_name_plural = u'Módulos'


class Reporte(models.Model):
    fecha = models.DateTimeField()
    fuente = models.CharField(max_length=200)
    descripcion = models.TextField()
    observaciones = models.TextField(null=True, blank=True)
    archivo = models.FileField(null=True, blank=True)

    modulo = models.ForeignKey(Modulo, related_name="reportes", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return str(self.fecha) + ' - ' + self.modulo.nombre + ' - ' + self.modulo.autor.nombres + ' ' +  self.modulo.autor.apellidos

    class Meta:
        verbose_name = u'Reporte'
        verbose_name_plural = u'Reportes'


class TipoContacto(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = u'Tipo de contacto'
        verbose_name_plural = u'Tipos de contacto'


class Contacto(models.Model):
    fecha = models.DateTimeField()
    descripcion = models.TextField()
    observaciones = models.TextField(null=True, blank=True)

    modulo = models.ForeignKey(Modulo, related_name="contactos", on_delete=models.PROTECT)
    tipo_contacto = models.ForeignKey(TipoContacto, related_name="contactos", on_delete=models.PROTECT)


    def __str__(self):
        return str(self.fecha) + ' - ' + self.tipo_contacto.nombre

    class Meta:
        verbose_name = u'Contacto'
        verbose_name_plural = u'Contactos'
