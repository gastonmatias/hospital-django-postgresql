from django.urls import path
from .views import home, registrarPaciente, listarPacientes, actualizarPaciente, eliminarPaciente

#nombre para luego evocar links  en los nav del html
app_name='app_web'

urlpatterns = [
    path('home/',home,name='home'),
    path('registrar-paciente/',registrarPaciente,name='registrarPaciente'),
    path('listar-pacientes/',listarPacientes,name='listarPacientes'),
    path('actualizar-paciente/<id>/',actualizarPaciente,name='actualizarPaciente'), 
    path('eliminar-paciente/<id>/',eliminarPaciente,name='eliminarPaciente'), 

]
