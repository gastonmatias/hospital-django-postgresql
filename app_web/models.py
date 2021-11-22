from django.db import models
from django.core.exceptions import  ValidationError

# Create your models here.
class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=25)
    apellido = models.CharField('Apellido',max_length=25)
    rut = models.CharField('Rut (Sin puntos, con guión)',max_length=12, unique=True)
    fecha_nacimiento = models.DateField('Fecha Nacimiento (dd/mm/aaaa)',null='true',blank=True)
    nacionalidad = models.CharField('Nacionalidad',max_length=200,null='true',blank=True)
    descripcion = models.CharField('Descripcion',max_length=300,null='true',blank=True)
    nickname = models.CharField('Nickname',max_length=20,null='true',blank=True)
    email = models.EmailField('Correo electronico', unique=True)
    password = models.CharField('Contraseña',max_length = 15)
    telefono = models.CharField('Telefono',max_length = 15)
    celular = models.CharField('Celular',max_length = 15)
    archivo = models.IntegerField('Archivo',null='true',blank=True)
    estado = models.CharField('Estado',max_length=50,null='true',blank=True)
    foto = models.ImageField('Fotografia (Opcional)',upload_to='fotos',null=True, blank='True', default='profile_default.jpg')

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    def clean(self):
        if self.nombre == 'jeje':
            raise ValidationError('Debe rellenar todos los campos obligatorios!')

