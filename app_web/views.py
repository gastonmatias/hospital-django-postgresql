from django.shortcuts import render, get_object_or_404, redirect
#importacion forms creados
from app_web.forms import PacienteForm
from app_web.models import Paciente
from django.contrib import messages
from django.core.paginator import Paginator #paginador de listado de pacientes
from django.http import Http404 # por si el "try - except" del paginador falla

from django.views.generic import ListView,View

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

def listarPacientes2(request):
    #pacientes_list = Paciente.objects.get_queryset().order_by('id_paciente')
    pacientes_list = Paciente.objects.all()
   
    data ={
        'pacientes': pacientes_list 
        #se optó por poner de nombre "entity" (y no 'productos')para que hiciera match con las validaciones
        #del archivo paginator.html
        #'paginator': paginator #enviar instancia de paginator, esta integrado con bootstrap
    }

    return render(request,'listar-pacientes.html',data)

def listarPacientes(request):
    #pacientes2 = Paciente.objects.get_queryset().order_by('id_paciente')
    pacientes2 = Paciente.objects.all().order_by('id_paciente')
    #para paginacion
    page = request.GET.get('page',1) #de la variable de la url, obtener la variable llamada page, 
                                     #si no existiese, se usará "1" por defecto (osea ir a la primera pagina por default)

    try: #try pq se puede caer si es que no existiese la pagina, por ejemplo
        paginator = Paginator(pacientes2,4)# 2 parametros = datos a paginar, cantidad de instancias
        pacientes2 = paginator.page(page)
    except:
        raise Http404 #si no existiese la pagina, se mostrará "not found"

    data ={
        'entity': pacientes2 
        #se optó por poner de nombre "entity" (y no 'productos')para que hiciera match con las validaciones
        #del archivo paginator.html
        #'paginator': paginator #enviar instancia de paginator, esta integrado con bootstrap
    }

    return render(request,'listar-pacientes2.html',data)

#############################################################################################
class ListarPacientes3(ListView):
    model = Paciente
    paginate_by = 5
    template_name = 'listar-pacientes3.html'
    ordering = ['id_paciente']
    #ordering_fields = ['nombre']

    def get_queryset(self):
        #pacientes_list = Paciente.objects.get_queryset().order_by('id_paciente')
        #pacientes3 = Paciente.objects.all()
        pacientes3 = Paciente.objects.get_queryset()
        return pacientes3

class ListarPacientes4(ListView):
    model = Paciente
    paginate_by = 5
    template_name = 'listar-pacientes4.html'
 

    def get_queryset(self):
        #pacientes_list = Paciente.objects.get_queryset().order_by('id_paciente')
        pacientes4 = Paciente.objects.all()
        return pacientes4
    
    def get_ordering(self):
        ordering = self.request.GET.get('ordering','telefono')
        # validate ordering here
        return ordering



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