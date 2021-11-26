from django.urls import path
from .views import home, registrarPaciente, listarPacientes, actualizarPaciente, eliminarPaciente, listarPacientes2, ListarPacientes3,ListarPacientes4

#nombre para luego evocar links  en los nav del html
app_name='app_web'

urlpatterns = [
    path('home/',home,name='home'),
    path('registrar-paciente/',registrarPaciente,name='registrarPaciente'),
    path('listar-pacientes/',listarPacientes,name='listarPacientes'),
    path('listar-pacientes2/',listarPacientes2,name='listarPacientes2'),
    path('listar-pacientes3/',ListarPacientes3.as_view(),name='ListarPacientes3'),
    path('listar-pacientes4/',ListarPacientes4.as_view(),name='ListarPacientes4'),
    path('actualizar-paciente/<id>/',actualizarPaciente,name='actualizarPaciente'), 
    path('eliminar-paciente/<id>/',eliminarPaciente,name='eliminarPaciente'), 

]
