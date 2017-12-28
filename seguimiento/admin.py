from django.contrib import admin
from .models import Autor, Asesor, Par, Modulo, Reporte, TipoContacto, Contacto

admin.site.register(Autor)
admin.site.register(Asesor)
admin.site.register(Par)
#admin.site.register(Modulo)
admin.site.register(Reporte)
admin.site.register(TipoContacto)
admin.site.register(Contacto)


class ContactosInLine(admin.TabularInline):
    model = Contacto
    extra = 0

class ReportesInLine(admin.TabularInline):
    model = Reporte
    extra = 0

@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'autor',
        'asesor',
        'par',
        'porcentaje_avance',
        '_cantidad_contactos'
   )
    list_select_related = (
        'autor',
   )
    inlines = [
        ReportesInLine,
        ContactosInLine
    ]
    
    def _cantidad_contactos(self, obj):
        return obj.contactos.all().count()