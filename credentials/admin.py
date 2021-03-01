from django.contrib import admin
from . models import usuarios
# Register your models here.
class UsuariosAdmin(admin.ModelAdmin):
    list_display = (
        'primer_nombre',
        'segundo_nombre',
        'primer_apellido',
        'segundo_apellido',
        'curso',
        'nip',
        'email',
        'password',
        'usuario_abaco',
        'clave_abaco',
    )


admin.site.register(usuarios, UsuariosAdmin)