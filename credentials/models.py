from django.db import models

# Create your models here.
class usuarios(models.Model):
    primer_nombre = models.CharField('Primer nombre',max_length=50)
    segundo_nombre = models.CharField('Segundo Nombre', max_length=50, blank=True)
    primer_apellido = models.CharField('Primer apellido', max_length=50)
    segundo_apellido = models.CharField('Segundo apellido', max_length=50, blank=True)
    curso = models.CharField('curso', max_length=5, blank=True)
    nip = models.BigIntegerField('documento', blank=True)
    email = models.CharField('correo institucional', max_length=100, blank=True)
    password = models.CharField('clave', max_length=50, blank=True)
    usuario_abaco = models.CharField('Usuario ABaco', max_length=100, blank=True)
    clave_abaco = models.CharField('clave ABaco', max_length=50, blank=True)

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return self.primer_nombre + '_' + self.primer_apellido