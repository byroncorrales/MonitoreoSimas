# -*- coding: UTF-8 -*-

from django.contrib import admin
from simas.models import *

class EducacionInline(admin.TabularInline):
    model = Educacion
    extra = 1
    max_num = 6
    
class SaludInline(admin.TabularInline):
    model = Salud
    extra = 1
    max_num = 6
    
class EnergiaInline(admin.TabularInline):
    model = Energia
    extra = 1
    max_num = 6
    
class AguaInline(admin.TabularInline):
    model = Agua
    extra = 1
    
class OrganizacionGremialInline(admin.TabularInline):
    model = OrganizacionGremial
    extra = 1
    
class OrganizacionComunitariaInline(admin.TabularInline):
    model = OrganizacionComunitaria
    extra = 1
    
class TenenciaInline(admin.TabularInline):
    model = Tenencia
    extra = 1
    
class UsoTierraInline(admin.TabularInline):
    model = UsoTierra
    extra = 1
    
class ExistenciaArbolesInline(admin.TabularInline):
    model = ExistenciaArboles
    extra = 1
    
class ReforestacionInline(admin.TabularInline):
    model = Reforestacion
    extra = 1
    
class AnimalesFincaInline(admin.TabularInline):
    model = AnimalesFinca
    extra = 1
    
class CultivosFincaInline(admin.TabularInline):
    model = CultivosFinca
    extra = 1
    
class OpcionesManejoInline(admin.TabularInline):
    model= OpcionesManejo
    extra = 1
    
class SemillaInline(admin.TabularInline):
    model = Semilla
    extra = 1
    
class SueloInline(admin.TabularInline):
    model = Suelo
    extra = 1
    
class ManejoSueloInline(admin.TabularInline):
    model = ManejoSuelo
    extra = 1
    
class IngresoFamiliarInline(admin.TabularInline):
    model = IngresoFamiliar
    extra = 1
    
class OtrosIngresosInline(admin.TabularInline):
    model = OtrosIngresos
    extra = 1
    
class TipoCasaInline(admin.TabularInline):
    model = TipoCasa
    extra = 1
    
class DetalleCasaInline(admin.TabularInline):
    model = DetalleCasa
    extra = 1
    
class PropiedadesInline(admin.TabularInline):
    model = Propiedades
    extra = 1
    
class HerramientasInline(admin.TabularInline):
    model = Herramientas
    extra = 1
    
class TransporteInline(admin.TabularInline):
    model = Transporte
    extra = 1
    
class AhorroInline(admin.TabularInline):
    model = Ahorro
    extra = 1
    
class CreditoInline(admin.TabularInline):
    model = Credito
    extra = 1
    
class SeguridadInline(admin.TabularInline):
    model = Seguridad
    extra = 1
    
class VulnerableInline(admin.TabularInline):
    model = Vulnerable
    extra = 1
    
class RiegosInline(admin.TabularInline):
    model = Riegos
    extra = 1
    
class EncuestaAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    inlines = [EducacionInline, SaludInline, EnergiaInline, AguaInline,
               OrganizacionGremialInline, OrganizacionComunitariaInline,
               TenenciaInline, UsoTierraInline, ExistenciaArbolesInline,
               ReforestacionInline, AnimalesFincaInline, CultivosFincaInline,
               OpcionesManejoInline, SemillaInline, SueloInline, ManejoSueloInline,
               IngresoFamiliarInline, OtrosIngresosInline, TipoCasaInline,
               DetalleCasaInline, PropiedadesInline, HerramientasInline,
               TransporteInline, AhorroInline, CreditoInline, SeguridadInline,
               VulnerableInline, RiegosInline,
               ]
    list_display = ('nombre', 'finca', 'comunidad', 'organizacion')
    list_filter = ['comunidad', 'organizacion']
    search_fields = ['nombre', 'comunidad__nombre', 'organizacion__nombre']
               
admin.site.register(Encuesta, EncuestaAdmin)

#-------------------------------------------

admin.site.register(Recolector)
admin.site.register(Organizaciones)
admin.site.register(PreguntaEnergia)
admin.site.register(Fuente)
admin.site.register(Tratamiento)
admin.site.register(Disponibilidad)
admin.site.register(OrgGremiales)
admin.site.register(BeneficiosObtenido)
admin.site.register(SerMiembro)
admin.site.register(OrgComunitarias)
admin.site.register(BeneficioOrgComunitaria)
admin.site.register(NoOrganizado)
admin.site.register(Uso)
admin.site.register(Maderable)
admin.site.register(Forrajero)
admin.site.register(Energetico)
admin.site.register(Frutal)
admin.site.register(Actividad)
admin.site.register(Animales)
admin.site.register(ProductoAnimal)
admin.site.register(Cultivos)
admin.site.register(ManejoAgro)
admin.site.register(CultivosVariedad)
admin.site.register(Variedades)
admin.site.register(Textura)
admin.site.register(Profundidad)
admin.site.register(Densidad)
admin.site.register(Pendiente)
admin.site.register(Drenaje)
admin.site.register(Preparar)
admin.site.register(Traccion)
admin.site.register(Fertilizacion)
admin.site.register(Conservacion)
admin.site.register(Rubros)
admin.site.register(Fuentes)
admin.site.register(TipoTrabajo)
admin.site.register(Piso)
admin.site.register(Techo)
admin.site.register(Equipos)
admin.site.register(Infraestructuras)
admin.site.register(NombreHerramienta)
admin.site.register(NombreTransporte)
admin.site.register(DaCredito)
admin.site.register(OcupaCredito)
admin.site.register(Alimentos)
admin.site.register(PreguntaRiesgo)
admin.site.register(Causa)
admin.site.register(Fenomeno)
admin.site.register(Graves)
