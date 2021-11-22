from django.shortcuts import render, get_object_or_404, redirect
#importacion forms creados
from app_web.forms import PacienteForm
from app_web.models import Paciente
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def registrarPaciente(request):
    #se instancia el form creado en forms.py para incrustarlo en registro-paciente.html
    data = {
        'form_paciente': PacienteForm()
    }

    # los inputs del formulario de registro rellenados por algun usuario 
    # llegan devuelta a esta vista "def registrarPaciente(request)", 
    
    # ahora se busca qe si los datos de estos inputs
    # son validados mediante el metodo post, entonces guardará estos datos
    # en la bd
    if request.method == 'POST':
        formulario = PacienteForm(data=request.POST, files=request.FILES)

        #si pasa la prueba de metodo post + SI pasa validaciones de form...
        if formulario.is_valid():
            formulario.save() #se guarda contenido en la bd
            messages.success(request,"Paciente Registrado!")
            return redirect(to='app_web:listarPacientes')
        # si pasa la prueba de metodo post + NO pasa validaciones de form...
        else:
            data["form_paciente"] = formulario#se sobreescribe el form en el html, para volver a intentarlo una vez mas
    
    return render (request,'registrar-paciente.html',data)#'data' se pasa como 3ra parametro para qe se imprima el form en el html

def listarPacientes(request):
    pacientes = Paciente.objects.all()

    data ={
        'pacientes': pacientes
    }

    return render(request,'listar-pacientes.html',data)

"""ACTUALIZAR PACIENTE"""
def actualizarPaciente(request, id):
    
    #se instancia objeto de bd que se actualizará
    paciente = get_object_or_404(Paciente, id_paciente=id) 

    data = {
        'form_actualizar' : PacienteForm(instance=paciente)#se instancia un formulario rellenado con datos
    }

    if request.method == 'POST':
        formulario = PacienteForm(data=request.POST, instance=paciente, files=request.FILES)#se pasa la instancia nuevamente para obtener la id del pacuente a modificar  
        
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Paciente Actualizado!") 
            return redirect(to='app_web:listarPacientes')
         # si pasa la prueba de metodo post + NO pasa validaciones de form...
        else:
            data["form_actualizar"] = formulario#se sobreescribe el form en el html, para volver a intentarlo una vez mas
    
    return render(request,'actualizar-paciente.html',data)

#ELIMINAR PACIENTE
def eliminarPaciente(request,id):
    paciente = get_object_or_404(Paciente, id_paciente=id) 
    paciente.delete()
    messages.success(request,"Paciente Eliminado!") 
    return redirect (to='app_web:listarPacientes')