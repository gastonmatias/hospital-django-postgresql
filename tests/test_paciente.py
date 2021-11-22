#importacion libreria a utilizar
import pytest
#importacion modelo bd que se usara para el test
from app_web.models import Paciente

#Unit Test Crear Paciente
##@pytest.mark.django_db
def test_paciente_creation():
    paciente = Paciente.objects.create(
        nombre = 'paco',
        apellido =  'de lucia',
        rut = '312545-7',
        email = 'paquito@hotmail.com',
        telefono = '+440568456',
        celular = '+4405689456',
    )

    assert paciente.nombre == 'paco'

def test_paciente_creation2():
    paciente = Paciente.objects.create(
        nombre = 'anakin',
        apellido =  'skywalker',
        rut = '1234567',
        telefono = '+440568456',
        celular = '+4405689456',
    )

    assert paciente.nombre == 'anakin'

    """pacienteRep = Paciente.objects.create(
        nombre = 'tomas',
        apellido =  'gonzales',
        rut = '18456984-7',
        email = 'paquito@hotmail.com',
        telefono = '+440568456',
        celular = '+4405689456',
    )
    assert pacienteRep.email == 'paquito@hotmail.com' """""
    
## Para otorgar permiso de acceso a la bd para testing
# y de paso fix error:
# "RuntimeError: Database access not allowed..." al ejecutar "pytest" en terminal
@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass

## otra forma de otorgar acceso a bd:
## arriba de cada "def test" escribir "@pytest.mark.django_db"