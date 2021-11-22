from django import forms
from app_web.models import Paciente
from django.contrib.auth.forms import UserCreationForm
#se importa tabla usuario creada por defecto de django, para definirla en el customcreationform
#y demas agregarle mas parametros custom
from django.contrib.auth.models import User 

#formulario creacion paciente
class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ['nombre','apellido','rut','telefono','celular','email','nacionalidad','fecha_nacimiento','descripcion','foto','nickname']

#se podria hacer directamente un formulario de registro en views, pero se usara un custom desde aqui
#pq despues se podran hacer validaciones utiles, de igual manera se creará el formulario a partir
#del mismo que otorga django
class CustomUserCreationForm(UserCreationForm):
    #pass # se podria dejar solo esto "pass" y se crearia automaticamente el formulario base,
    #que pide nombre usuario-password1-password2

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

        #se le agregaron mas parametros para el formulario de registro, pero ojo, estos datos
        #YA EXISTEN en la tabla user, solo se evocaron


