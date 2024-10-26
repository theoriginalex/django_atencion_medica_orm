"""
comando pra el orm:
python manage.py shell_plus
"""
from aplication.core.models import *
from aplication.attention.models import *
from django.db.models import Q
from django.db.models import Sum,Avg,Max,Min,Count
from django.db.models import F
# insertar registro directamente
tipo1 = TipoSangre.objects.create(tipo="C+", descripcion="Tipo C positivo")

"""
In [18]: tipo1 = TipoSangre.objects.create(tipo="C+", descripcion="Tipo C positivo")
INSERT INTO "core_tiposangre" ("tipo", "descripcion")
VALUES ('C+', 'Tipo C positivo') RETURNING "core_tiposangre"."id"

Execution time: 0.002123s [Database: default]

In [19]: tipo1
Out[19]: <TipoSangre: C+>

"""


# crea el registro en memoria
tipo2 = TipoSangre(tipo="C-", descripcion="Tipo C negativo")
tipo2.save()  # Y luego con save() lo guarda el registro en la base de datos
"""
In [21]: tipo2 = TipoSangre(tipo="C-", descripcion="Tipo C negativo")

In [22]: tipo2.save()
INSERT INTO "core_tiposangre" ("tipo", "descripcion")
VALUES ('C-', 'Tipo C negativo') RETURNING "core_tiposangre"."id"

Execution time: 0.001000s [Database: default]

In [23]: tipo2
Out[23]: <TipoSangre: C->
"""


# Crea una lista de instancias de TipoSangre con varios tipos de sangre
tipos_sangre = [
    TipoSangre(tipo="B+", descripcion="Tipo B positivo"),
    TipoSangre(tipo="A-", descripcion="Tipo A negativo"),
]
"""
In [3]: tipos_sangre = [
   ...:     TipoSangre(tipo="B+", descripcion="Tipo B positivo"),
   ...:     TipoSangre(tipo="A-", descripcion="Tipo A negativo"),
   ...: ]

In [4]: tipos_sangre
Out[4]: [<TipoSangre: B+>, <TipoSangre: A->]
"""
# inserta registro de forma maxima directamente en la basedato
TipoSangre.objects.bulk_create(tipos_sangre)
"""
In [2]: TipoSangre.objects.bulk_create(tipos_sangre)
BEGIN

Execution time: 0.000000s [Database: default]
INSERT INTO "core_tiposangre" ("tipo", "descripcion")
VALUES ('B+', 'Tipo B positivo'), ('A-', 'Tipo A negativo') RETURNING "core_tiposangre"."id"

Execution time: 0.001000s [Database: default]
Out[2]: [<TipoSangre: B+>, <TipoSangre: A->]
"""
# Consulta todos los registros de TipoSangre con todos sus campos
tipos_sangre = TipoSangre.objects.all()

# Imprimir los resultados
for tipo in tipos_sangre:
    print(f"Tipo: {tipo.tipo}, Descripción: {tipo.descripcion}")

"""
In [3]: tipos_sangre = TipoSangre.objects.all()

In [4]: for tipo in tipos_sangre:
   ...:     print(f"Tipo: {tipo.tipo}, Descripción: {tipo.descripcion}")
   ...:
SELECT "core_tiposangre"."id",
       "core_tiposangre"."tipo",
       "core_tiposangre"."descripcion"
  FROM "core_tiposangre"

Execution time: 0.000000s [Database: default]
Tipo: A, Descripción: Tipo A
Tipo: O-, Descripción: O negativo
Tipo: AB+, Descripción: tipo Ab+
Tipo: B-, Descripción: Tipo B negativo
Tipo: O+, Descripción: Tipo O positivo
Tipo: C+, Descripción: Tipo C positivo
Tipo: C-, Descripción: Tipo C negativo
Tipo: B+, Descripción: Tipo B positivo
Tipo: A-, Descripción: Tipo A negativo
"""
# Selecciona los tipos de sangre    
tipo_O_pos = TipoSangre.objects.get(tipo="O+")
tipo_A = TipoSangre.objects.get(tipo="A")
tipo_ab_pos = TipoSangre.objects.get(tipo="AB+")
"""
In [5]: tipo_O_pos = TipoSangre.objects.get(tipo="O+")
   ...: tipo_A = TipoSangre.objects.get(tipo="A")
   ...: tipo_ab_pos = TipoSangre.objects.get(tipo="AB+")
SELECT "core_tiposangre"."id",
       "core_tiposangre"."tipo",
       "core_tiposangre"."descripcion"
  FROM "core_tiposangre"
 WHERE "core_tiposangre"."tipo" = 'O+'
 LIMIT 21

Execution time: 0.000000s [Database: default]
SELECT "core_tiposangre"."id",
       "core_tiposangre"."tipo",
       "core_tiposangre"."descripcion"
  FROM "core_tiposangre"
 WHERE "core_tiposangre"."tipo" = 'A'
 LIMIT 21

Execution time: 0.000000s [Database: default]
SELECT "core_tiposangre"."id",
       "core_tiposangre"."tipo",
       "core_tiposangre"."descripcion"
  FROM "core_tiposangre"
 WHERE "core_tiposangre"."tipo" = 'AB+'
 LIMIT 21

Execution time: 0.000000s [Database: default]
"""
# Se Crea una lista de instancias de Paciente
pacientes = [
    Paciente(
        nombres="Juan",
        apellidos="Pérez",
        cedula="1234567890",
        fecha_nacimiento="1980-01-15",
        telefono="0998765432",
        email="juan.perez@example.com",
        sexo="M",
        estado_civil="C",
        direccion="Calle Falsa 123",
        latitud=-0.123456,
        longitud=-78.123456,
        tipo_sangre=tipo_O_pos,
        alergias="Ninguna",
        enfermedades_cronicas="Hipertensión",
        medicacion_actual="Losartán",
        cirugias_previas="Apendicectomía",
        antecedentes_personales="Diabetes en tratamiento",
        antecedentes_familiares="Corazón en la familia"
    ),
    Paciente(
        nombres="María",
        apellidos="Gómez",
        cedula="0987654321",
        fecha_nacimiento="1990-05-20",
        telefono="0991234567",
        email="maria.gomez@example.com",
        sexo="F",
        estado_civil="S",
        direccion="Av. Libertad 456",
        latitud=-0.654321,
        longitud=-78.654321,
        tipo_sangre=tipo_A,
        alergias="Penicilina",
        enfermedades_cronicas="Asma",
        medicacion_actual="Salbutamol",
        cirugias_previas="Ninguna",
        antecedentes_personales="No fuma",
        antecedentes_familiares="Madre con cáncer"
    ),
    Paciente(
        nombres="Carlos",
        apellidos="Ramírez",
        cedula="1357924680",
        fecha_nacimiento="1975-09-30",
        telefono="0987654321",
        email="carlos.ramirez@example.com",
        sexo="M",
        estado_civil="C",
        direccion="Calle 10 de Agosto 789",
        latitud=-0.321654,
        longitud=-78.321654,
        tipo_sangre=tipo_ab_pos,
        alergias="Ninguna",
        enfermedades_cronicas="Ninguna",
        medicacion_actual="Ninguna",
        cirugias_previas="Ninguna",
        antecedentes_personales="No antecedentes relevantes",
        antecedentes_familiares="Padre con hipertensión"
    ),
]
# Insercion maxiva de los registros en la base de datos utilizando bulk_create
Paciente.objects.bulk_create(pacientes)
""" 
In [11]: Paciente.objects.bulk_create(pacientes)
BEGIN

Execution time: 0.000000s [Database: default]
INSERT INTO "core_paciente" ("nombres", "apellidos", "cedula", "fecha_nacimiento", "telefono", "email", "sexo", "estado_civil", "direccion", "latitud", "longitud", "tipo_sangre_id", "alergias", "enfermedades_cronicas", "medicacion_actual", "cirugias_previas", "antecedentes_personales", "antecedentes_familiares")
VALUES ('Juan', 'Pérez', '1234567891', '1980-01-15', '0998765432', 'juan.perez@example.com', 'M', 'C', 'Calle Falsa 123', '-0.123456', '-78.123456', 23, 'Ninguna', 'Hipertensión', 'Losartán', 'Apendicectomía', 'Diabetes en tratamiento', 'Corazón en la familia'), ('María', 'Gómez', '0987654322', '1990-05-20', '0991234567', 'maria.gomez@example.com', 'F', 'S', 'Av. Libertad 456', '-0.654321', '-78.654321', 2, 'Penicilina', 'Asma', 'Salbutamol', 'Ninguna', 'No fuma', 'Madre con cáncer'), ('Carlos',
       'Ramírez',
       '1357924683',
       '1975-09-30',
       '0987654321',
       'carlos.ramirez@example.com',
       'M',
       'C',
       'Calle 10 de Agosto 789',
       '-0.321654',
       '-78.321654',
       16,
       'Ninguna',
       'Ninguna',
       'Ninguna', 'N

Execution time: 0.002098s [Database: default]
Out[11]: [<Paciente: Juan>, <Paciente: María>, <Paciente: Carlos>]
"""
# Presenta todos los pacientes 
pacientes=Paciente.objects.all()
for paciente in pacientes:
    print(f"--- Paciente ---")
    print(f"Nombres: {paciente.nombres}")
    print(f"Apellidos: {paciente.apellidos}")
    print(f"Cédula: {paciente.cedula}")
    print(f"Fecha de Nacimiento: {paciente.fecha_nacimiento}")
    print(f"Teléfono: {paciente.telefono}")
    print(f"Email: {paciente.email}")
    print(f"Sexo: {paciente.sexo}")
    print(f"Estado Civil: {paciente.estado_civil}")
    print(f"Dirección: {paciente.direccion}")
    print(f"Latitud: {paciente.latitud}")
    print(f"Longitud: {paciente.longitud}")
    print(f"Tipo de Sangre: {paciente.tipo_sangre.tipo if paciente.tipo_sangre else 'No especificado'}")
    print(f"Alergias: {paciente.alergias if paciente.alergias else 'Ninguna'}")
    print(f"Enfermedades Crónicas: {paciente.enfermedades_cronicas if paciente.enfermedades_cronicas else 'Ninguna'}")
    print(f"Medicación Actual: {paciente.medicacion_actual if paciente.medicacion_actual else 'Ninguna'}")
    print(f"Cirugías Previas: {paciente.cirugias_previas if paciente.cirugias_previas else 'Ninguna'}")
    print(f"Antecedentes Personales: {paciente.antecedentes_personales if paciente.antecedentes_personales else 'Ninguno'}")
    print(f"Antecedentes Familiares: {paciente.antecedentes_familiares if paciente.antecedentes_familiares else 'Ninguno'}")
    print("-----------------------------")
""" 
In [12]: pacientes=Paciente.objects.all()

In [13]: for paciente in pacientes:
    ...:     print(f"--- Paciente ---")
    ...:     print(f"Nombres: {paciente.nombres}")
    ...:     print(f"Apellidos: {paciente.apellidos}")
    ...:     print(f"Cédula: {paciente.cedula}")
    ...:     print(f"Fecha de Nacimiento: {paciente.fecha_nacimiento}")
    ...:     print(f"Teléfono: {paciente.telefono}")
    ...:     print(f"Email: {paciente.email}")
    ...:     print(f"Sexo: {paciente.sexo}")
    ...:     print(f"Estado Civil: {paciente.estado_civil}")
    ...:     print(f"Dirección: {paciente.direccion}")
    ...:     print(f"Latitud: {paciente.latitud}")
    ...:     print(f"Longitud: {paciente.longitud}")
    ...:     print(f"Tipo de Sangre: {paciente.tipo_sangre.tipo if paciente.tipo_sangre else 'No especificado'}")
    ...:     print(f"Alergias: {paciente.alergias if paciente.alergias else 'Ninguna'}")
    ...:     print(f"Enfermedades Crónicas: {paciente.enfermedades_cronicas if paciente.enfermedades_cronicas else 'Ninguna'}")
    ...:     print(f"Medicación Actual: {paciente.medicacion_actual if paciente.medicacion_actual else 'Ninguna'}")
    ...:     print(f"Cirugías Previas: {paciente.cirugias_previas if paciente.cirugias_previas else 'Ninguna'}")
    ...:     print(f"Antecedentes Personales: {paciente.antecedentes_personales if paciente.antecedentes_personales else 'Ninguno'}")
    ...:     print(f"Antecedentes Familiares: {paciente.antecedentes_familiares if paciente.antecedentes_familiares else 'Ninguno'}")
    ...:     print("-----------------------------")
    ...:
SELECT "core_paciente"."id",
       "core_paciente"."nombres",
       "core_paciente"."apellidos",
       "core_paciente"."cedula",
       "core_paciente"."fecha_nacimiento",
       "core_paciente"."telefono",
       "core_paciente"."email",
       "core_paciente"."sexo",
       "core_paciente"."estado_civil",
       "core_paciente"."direccion",
       "core_paciente"."latitud",
       "core_paciente"."longitud",
       "core_paciente"."tipo_sangre_id",
       "core_paciente"."alergias",
       "core_paciente"."enfermedades_cronicas",
       "core_paciente"."medicacion_actual",
       "core_paciente"."cirugias_previas",
       "core_paciente"."antecedentes_personales",
       "core_paciente"."antecedentes_familiares"
  FROM "core_paciente"
 ORDER BY "core_paciente"."apellidos" ASC

Execution time: 0.000000s [Database: default]
--- Paciente ---
Nombres: Yadira
Apellidos: Bohorquez
Cédula: 0914192184
Fecha de Nacimiento: 2024-10-15
Teléfono: 434445434
Email: yb@gmail.com
Sexo: F
Estado Civil: C
Dirección: Milagro
Latitud: 12232.340000
Longitud: 344.550000
Tipo de Sangre: No especificado
Alergias: al povo
Enfermedades Crónicas: ninguna
Medicación Actual: alegra D
Cirugías Previas: nariz
Antecedentes Personales: estres
Antecedentes Familiares: hipetension
-----------------------------
--- Paciente ---
Nombres: Wilmer
Apellidos: Camino
Cédula: 0914192186
Fecha de Nacimiento: 2024-10-16
Teléfono: 34545454 - 56656565
Email: ca@gmail.com
Sexo: M
Estado Civil: C
Dirección: Milagro
Latitud: 23334.556000
Longitud: 455445.545400
SELECT "core_tiposangre"."id",
       "core_tiposangre"."tipo",
       "core_tiposangre"."descripcion"
  FROM "core_tiposangre"
 WHERE "core_tiposangre"."id" = 16
 LIMIT 21

Execution time: 0.000000s [Database: default]
Tipo de Sangre: AB+
Alergias: ninguna
Enfermedades Crónicas: cancer
Medicación Actual: ampicilina
Cirugías Previas: corazon abierto
Antecedentes Personales: diabetis
Antecedentes Familiares: hipertension
-----------------------------
--- Paciente ---
Nombres: María
Apellidos: Gómez
Cédula: 0987654321
Fecha de Nacimiento: 1990-05-20
Teléfono: 0991234567
Email: maria.gomez@example.com
Sexo: F
Estado Civil: S
Dirección: Av. Libertad 456
Latitud: -0.654321
Longitud: -78.654321
Tipo de Sangre: No especificado
Alergias: Penicilina
Enfermedades Crónicas: Asma
Medicación Actual: Salbutamol
Cirugías Previas: Ninguna
Antecedentes Personales: No fuma
Antecedentes Familiares: Madre con cáncer
-----------------------------
--- Paciente ---
Nombres: María
Apellidos: Gómez
Cédula: 0987654322
Fecha de Nacimiento: 1990-05-20
Teléfono: 0991234567
Email: maria.gomez@example.com
Sexo: F
Estado Civil: S
Dirección: Av. Libertad 456
Latitud: -0.654321
Longitud: -78.654321
SELECT "core_tiposangre"."id",
       "core_tiposangre"."tipo",
       "core_tiposangre"."descripcion"
  FROM "core_tiposangre"
 WHERE "core_tiposangre"."id" = 2
 LIMIT 21

Execution time: 0.000000s [Database: default]
Tipo de Sangre: A
Alergias: Penicilina
Enfermedades Crónicas: Asma
Medicación Actual: Salbutamol
Cirugías Previas: Ninguna
Antecedentes Personales: No fuma
Antecedentes Familiares: Madre con cáncer
-----------------------------
--- Paciente ---
Nombres: Juan
Apellidos: Pérez
Cédula: 1234567890
Fecha de Nacimiento: 1980-01-15
Teléfono: 0998765432
Email: juan.perez@example.com
Sexo: M
Estado Civil: C
Dirección: Calle Falsa 123
Latitud: -0.123456
Longitud: -78.123456
SELECT "core_tiposangre"."id",
       "core_tiposangre"."tipo",
       "core_tiposangre"."descripcion"
  FROM "core_tiposangre"
 WHERE "core_tiposangre"."id" = 2
 LIMIT 21

Execution time: 0.000000s [Database: default]
Tipo de Sangre: A
Alergias: Ninguna
Enfermedades Crónicas: Hipertensión
Medicación Actual: Losartán
Cirugías Previas: Apendicectomía
Antecedentes Personales: Diabetes en tratamiento
Antecedentes Familiares: Corazón en la familia
-----------------------------
--- Paciente ---
Nombres: Juan
Apellidos: Pérez
Cédula: 1234567891
Fecha de Nacimiento: 1980-01-15
Teléfono: 0998765432
Email: juan.perez@example.com
Sexo: M
Estado Civil: C
Dirección: Calle Falsa 123
Latitud: -0.123456
Longitud: -78.123456
SELECT "core_tiposangre"."id",
       "core_tiposangre"."tipo",
       "core_tiposangre"."descripcion"
  FROM "core_tiposangre"
 WHERE "core_tiposangre"."id" = 23
 LIMIT 21

Execution time: 0.000000s [Database: default]
Tipo de Sangre: O+
Alergias: Ninguna
Enfermedades Crónicas: Hipertensión
Medicación Actual: Losartán
Cirugías Previas: Apendicectomía
Antecedentes Personales: Diabetes en tratamiento
Antecedentes Familiares: Corazón en la familia
-----------------------------
--- Paciente ---
Nombres: Carlos
Apellidos: Ramírez
Cédula: 1357924680
Fecha de Nacimiento: 1975-09-30
Teléfono: 0987654321
Email: carlos.ramirez@example.com
Sexo: M
Estado Civil: C
Dirección: Calle 10 de Agosto 789
Latitud: -0.321654
Longitud: -78.321654
SELECT "core_tiposangre"."id",
       "core_tiposangre"."tipo",
       "core_tiposangre"."descripcion"
  FROM "core_tiposangre"
 WHERE "core_tiposangre"."id" = 16
 LIMIT 21

Execution time: 0.000000s [Database: default]
Tipo de Sangre: AB+
Alergias: Ninguna
Enfermedades Crónicas: Ninguna
Medicación Actual: Ninguna
Cirugías Previas: Ninguna
Antecedentes Personales: No antecedentes relevantes
Antecedentes Familiares: Padre con hipertensión
-----------------------------
--- Paciente ---
Nombres: Carlos
Apellidos: Ramírez
Cédula: 1357924683
Fecha de Nacimiento: 1975-09-30
Teléfono: 0987654321
Email: carlos.ramirez@example.com
Sexo: M
Estado Civil: C
Dirección: Calle 10 de Agosto 789
Latitud: -0.321654
Longitud: -78.321654
SELECT "core_tiposangre"."id",
       "core_tiposangre"."tipo",
       "core_tiposangre"."descripcion"
  FROM "core_tiposangre"
 WHERE "core_tiposangre"."id" = 16
 LIMIT 21

Execution time: 0.000000s [Database: default]
Tipo de Sangre: AB+
Alergias: Ninguna
Enfermedades Crónicas: Ninguna
Medicación Actual: Ninguna
Cirugías Previas: Ninguna
Antecedentes Personales: No antecedentes relevantes
Antecedentes Familiares: Padre con hipertensión
-----------------------------
"""
# Consulta pacientes con tipo de sangre O+
pacientes_o_plus = Paciente.objects.filter(tipo_sangre__tipo="O+")
"""
In [14]: pacientes_o_plus = Paciente.objects.filter(tipo_sangre__tipo="O+")

In [15]: pacientes_o_plus
Out[15]: SELECT "core_paciente"."id",
       "core_paciente"."nombres",
       "core_paciente"."apellidos",
       "core_paciente"."cedula",
       "core_paciente"."fecha_nacimiento",
       "core_paciente"."telefono",
       "core_paciente"."email",
       "core_paciente"."sexo",
       "core_paciente"."estado_civil",
       "core_paciente"."direccion",
       "core_paciente"."latitud",
       "core_paciente"."longitud",
       "core_paciente"."tipo_sangre_id",
       "core_paciente"."alergias",
       "core_paciente"."enfermedades_cronicas",
       "core_paciente"."medicacion_actual",
       "core_paciente"."cirugias_previas",
       "core_paciente"."antecedentes_personales",
       "core_paciente"."antecedentes_familiares"
  FROM "core_paciente"
 INNER JOIN "core_tiposangre"
    ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
 WHERE "core_tiposangre"."tipo" = 'O+'
 ORDER BY "core_paciente"."apellidos" ASC
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [<Paciente: Juan>]>
"""
# funciones para manejo de texto del orm de django
# exact (coincidencia exacta), 
# iexact (coincidencia exacta sin distinguir mayúsculas/minúsculas), 
# contains (contiene el contenido), 
# icontains (contiene el contenido sin distinguir mayúsculas/minúsculas), 
# startswith (comienza con el contenido), 
# istartswith (comienza con el contenido sin distinguir mayúsculas/minúsculas), 
# endswith (termina con el contenido), 
# iendswith (termina con el contenido sin distinguir mayúsculas/minúsculas), 
# regex (coincide con expresión regular), 
# iregex (coincide con expresión regular sin distinguir mayúsculas/minúsculas)

# Consulta pacientes que contengan 'O' en el tipo de sangre. Ejemplo icontains
pacientes_con_o = Paciente.objects.filter(tipo_sangre__tipo__icontains="O")
"""
In [16]: pacientes_con_o = Paciente.objects.filter(tipo_sangre__tipo__icontains="O")

In [17]: pacientes_con_o
Out[17]: SELECT "core_paciente"."id",
       "core_paciente"."nombres",
       "core_paciente"."apellidos",
       "core_paciente"."cedula",
       "core_paciente"."fecha_nacimiento",
       "core_paciente"."telefono",
       "core_paciente"."email",
       "core_paciente"."sexo",
       "core_paciente"."estado_civil",
       "core_paciente"."direccion",
       "core_paciente"."latitud",
       "core_paciente"."longitud",
       "core_paciente"."tipo_sangre_id",
       "core_paciente"."alergias",
       "core_paciente"."enfermedades_cronicas",
       "core_paciente"."medicacion_actual",
       "core_paciente"."cirugias_previas",
       "core_paciente"."antecedentes_personales",
       "core_paciente"."antecedentes_familiares"
  FROM "core_paciente"
 INNER JOIN "core_tiposangre"
    ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
 WHERE "core_tiposangre"."tipo" LIKE '%O%' ESCAPE '\'
 ORDER BY "core_paciente"."apellidos" ASC
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [<Paciente: Juan>]>
"""
# Buscar empleados cuyos nombres empiecen con una "y" o "w" sin importar mayúsculas/minúsculas
empleados_con_yw = Paciente.objects.filter(nombres__iregex=r'^[yw]')
"""
In [18]: empleados_con_yw = Paciente.objects.filter(nombres__iregex=r'^[yw]')

In [19]: empleados_con_yw
Out[19]: SELECT "core_paciente"."id",
       "core_paciente"."nombres",
       "core_paciente"."apellidos",
       "core_paciente"."cedula",
       "core_paciente"."fecha_nacimiento",
       "core_paciente"."telefono",
       "core_paciente"."email",
       "core_paciente"."sexo",
       "core_paciente"."estado_civil",
       "core_paciente"."direccion",
       "core_paciente"."latitud",
       "core_paciente"."longitud",
       "core_paciente"."tipo_sangre_id",
       "core_paciente"."alergias",
       "core_paciente"."enfermedades_cronicas",
       "core_paciente"."medicacion_actual",
       "core_paciente"."cirugias_previas",
       "core_paciente"."antecedentes_personales",
       "core_paciente"."antecedentes_familiares"
  FROM "core_paciente"
 WHERE "core_paciente"."nombres" REGEXP '(?i)' || '^[yw]'
 ORDER BY "core_paciente"."apellidos" ASC
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [<Paciente: Yadira>, <Paciente: Wilmer>]>
"""
# funciones de fecha del orm
# year: fecha__year=2024  o # (fecha__year__in=[2022, 2023, 2024]
# month: fecha__month=10 (para octubre)
# day: fecha__day=15
# week_day: fecha__week_day=1 (para domingo)
# quarter: fecha__quarter=2 (para el segundo trimestre)
# isnull: fecha__isnull=True (para comprobar si es NULL)
# gt: fecha__gt='2024-01-01' (mayor que una fecha específica)
# lt: fecha__lt='2024-01-01' (menor que una fecha específica)
# gte: fecha__gte='2024-01-01' (mayor o igual que una fecha específica)
# lte: fecha__lte='2024-01-01' (menor o igual que una fecha específica)
# range: fecha__range=['2024-01-01', '2024-12-31'] (dentro de un rango específico)
# Ejemplo
# presenta un queryset de pacientes como diccionarios (apellidos y fecha_nacimiento) que nacieron en 2024
pacientes_2024 = Paciente.objects.filter(fecha_nacimiento__year=2024).values('apellidos','fecha_nacimiento')
"""
In [20]: pacientes_2024 = Paciente.objects.filter(fecha_nacimiento__year=2024).values('apellidos','fecha_nacimiento')

In [21]: pacientes_2024
Out[21]: SELECT "core_paciente"."apellidos",
       "core_paciente"."fecha_nacimiento"
  FROM "core_paciente"
 WHERE "core_paciente"."fecha_nacimiento" BETWEEN '2024-01-01' AND '2024-12-31'
 ORDER BY "core_paciente"."apellidos" ASC
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [{'apellidos': 'Bohorquez', 'fecha_nacimiento': datetime.date(2024, 10, 15)}, {'apellidos': 'Camino', 'fecha_nacimiento': datetime.date(2024, 10, 16)}]>
"""
# Consulta pacientes que nacieron antes de 1980
# > __gt, < __lt, >= __gte, <= __lte, != __ne
pacientes_menor_2024 = Paciente.objects.filter(fecha_nacimiento__year__lt=2024).values('apellidos','fecha_nacimiento')
"""
In [22]: pacientes_menor_2024 = Paciente.objects.filter(fecha_nacimiento__year__lt=2024).values('apellidos','fecha_nacimiento')

In [23]: pacientes_menor_2024
Out[23]: SELECT "core_paciente"."apellidos",
       "core_paciente"."fecha_nacimiento"
  FROM "core_paciente"
 WHERE "core_paciente"."fecha_nacimiento" < '2024-01-01'
 ORDER BY "core_paciente"."apellidos" ASC
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [{'apellidos': 'Gómez', 'fecha_nacimiento': datetime.date(1990, 5, 20)}, {'apellidos': 'Gómez', 'fecha_nacimiento': datetime.date(1990, 5, 20)}, {'apellidos': 'Pérez', 'fecha_nacimiento': datetime.date(1980, 1, 15)}, {'apellidos': 'Pérez', 'fecha_nacimiento': datetime.date(1980, 1, 15)}, {'apellidos': 'Ramírez', 'fecha_nacimiento': datetime.date(1975, 9, 30)}, {'apellidos': 'Ramírez', 'fecha_nacimiento': datetime.date(1975, 9, 30)}]>
"""
# convierte el queryset a una lista de diccionarios
pacientes_menor_2024=list(pacientes_menor_2024)
"""
In [24]: pacientes_menor_2024=list(pacientes_menor_2024)
SELECT "core_paciente"."apellidos",
       "core_paciente"."fecha_nacimiento"
  FROM "core_paciente"
 WHERE "core_paciente"."fecha_nacimiento" < '2024-01-01'
 ORDER BY "core_paciente"."apellidos" ASC

Execution time: 0.000000s [Database: default]

In [25]: pacientes_menor_2024
Out[25]:
[{'apellidos': 'Gómez', 'fecha_nacimiento': datetime.date(1990, 5, 20)},
 {'apellidos': 'Gómez', 'fecha_nacimiento': datetime.date(1990, 5, 20)},
 {'apellidos': 'Pérez', 'fecha_nacimiento': datetime.date(1980, 1, 15)},
 {'apellidos': 'Pérez', 'fecha_nacimiento': datetime.date(1980, 1, 15)},
 {'apellidos': 'Ramírez', 'fecha_nacimiento': datetime.date(1975, 9, 30)},
 {'apellidos': 'Ramírez', 'fecha_nacimiento': datetime.date(1975, 9, 30)}]
"""
# Obtener los nombres y la descripción del tipo de sangre de pacientes con tipo de sangre "AB+"
pacientes_ab = Paciente.objects.filter(tipo_sangre__tipo="AB+").values('nombres', 'apellidos', 'tipo_sangre__descripcion')
"""
In [26]: pacientes_ab = Paciente.objects.filter(tipo_sangre__tipo="AB+").values('nombres', 'apellidos', 'tipo_sangre__descripcion')

In [27]: pacientes_ab
Out[27]: SELECT "core_paciente"."nombres",
       "core_paciente"."apellidos",
       "core_tiposangre"."descripcion"
  FROM "core_paciente"
 INNER JOIN "core_tiposangre"
    ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
 WHERE "core_tiposangre"."tipo" = 'AB+'
 ORDER BY "core_paciente"."apellidos" ASC
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [{'nombres': 'Wilmer', 'apellidos': 'Camino', 'tipo_sangre__descripcion': 'tipo Ab+'}, {'nombres': 'Carlos', 'apellidos': 'Ramírez', 'tipo_sangre__descripcion': 'tipo Ab+'}, {'nombres': 'Carlos', 'apellidos': 'Ramírez', 'tipo_sangre__descripcion': 'tipo Ab+'}]>
"""
# Obtener los tipos de sangre "AB+" y los nombres de los pacientes asociados
tipos_sangre_ab = TipoSangre.objects.filter(tipo="AB+").values('descripcion', 'tipos_sangre__nombres', 'tipos_sangre__apellidos')
"""
In [28]: tipos_sangre_ab = TipoSangre.objects.filter(tipo="AB+").values('descripcion', 'tipos_sangre__nombres', 'tipos_sangre__apellidos')

In [29]: tipos_sangre_ab
Out[29]: SELECT "core_tiposangre"."descripcion",
       "core_paciente"."nombres",
       "core_paciente"."apellidos"
  FROM "core_tiposangre"
  LEFT OUTER JOIN "core_paciente"
    ON ("core_tiposangre"."id" = "core_paciente"."tipo_sangre_id")
 WHERE "core_tiposangre"."tipo" = 'AB+'
 LIMIT 21

Execution time: 0.001038s [Database: default]
<QuerySet [{'descripcion': 'tipo Ab+', 'tipos_sangre__nombres': 'Wilmer', 'tipos_sangre__apellidos': 'Camino'}, {'descripcion': 'tipo Ab+', 'tipos_sangre__nombres': 'Carlos', 'tipos_sangre__apellidos': 'Ramírez'}, {'descripcion': 'tipo Ab+', 'tipos_sangre__nombres': 'Carlos', 'tipos_sangre__apellidos': 'Ramírez'}]>
"""
# consulta inversa
# Obtener el tipo de sangre "AB+"
tipo_sangre_ab = TipoSangre.objects.get(tipo="AB+")
"""
In [30]: tipo_sangre_ab = TipoSangre.objects.get(tipo="AB+")
SELECT "core_tiposangre"."id",
       "core_tiposangre"."tipo",
       "core_tiposangre"."descripcion"
  FROM "core_tiposangre"
 WHERE "core_tiposangre"."tipo" = 'AB+'
 LIMIT 21

Execution time: 0.000000s [Database: default]

In [31]: tipo_sangre_ab
Out[31]: <TipoSangre: AB+>
"""
# Obtener todos los pacientes que tienen este tipo de sangre
pacientes_con_ab = tipo_sangre_ab.tipos_sangre.all()
"""
In [32]: pacientes_con_ab = tipo_sangre_ab.tipos_sangre.all()

In [33]: pacientes_con_ab
Out[33]: SELECT "core_paciente"."id",
       "core_paciente"."nombres",
       "core_paciente"."apellidos",
       "core_paciente"."cedula",
       "core_paciente"."fecha_nacimiento",
       "core_paciente"."telefono",
       "core_paciente"."email",
       "core_paciente"."sexo",
       "core_paciente"."estado_civil",
       "core_paciente"."direccion",
       "core_paciente"."latitud",
       "core_paciente"."longitud",
       "core_paciente"."tipo_sangre_id",
       "core_paciente"."alergias",
       "core_paciente"."enfermedades_cronicas",
       "core_paciente"."medicacion_actual",
       "core_paciente"."cirugias_previas",
       "core_paciente"."antecedentes_personales",
       "core_paciente"."antecedentes_familiares"
  FROM "core_paciente"
 WHERE "core_paciente"."tipo_sangre_id" = 16
 ORDER BY "core_paciente"."apellidos" ASC
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [<Paciente: Wilmer>, <Paciente: Carlos>, <Paciente: Carlos>]>
"""
# Consulta con AND
pacientes = Paciente.objects.filter(fecha_nacimiento__year=1980, tipo_sangre__tipo="O+")
"""
In [34]: pacientes = Paciente.objects.filter(fecha_nacimiento__year=1980, tipo_sangre__tipo="O+")

In [35]: pacientes
Out[35]: SELECT "core_paciente"."id",
       "core_paciente"."nombres",
       "core_paciente"."apellidos",
       "core_paciente"."cedula",
       "core_paciente"."fecha_nacimiento",
       "core_paciente"."telefono",
       "core_paciente"."email",
       "core_paciente"."sexo",
       "core_paciente"."estado_civil",
       "core_paciente"."direccion",
       "core_paciente"."latitud",
       "core_paciente"."longitud",
       "core_paciente"."tipo_sangre_id",
       "core_paciente"."alergias",
       "core_paciente"."enfermedades_cronicas",
       "core_paciente"."medicacion_actual",
       "core_paciente"."cirugias_previas",
       "core_paciente"."antecedentes_personales",
       "core_paciente"."antecedentes_familiares"
  FROM "core_paciente"
 INNER JOIN "core_tiposangre"
    ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
 WHERE ("core_paciente"."fecha_nacimiento" BETWEEN '1980-01-01' AND '1980-12-31' AND "core_tiposangre"."tipo" = 'O+')
 ORDER BY "core_paciente"."apellidos" ASC
 LIMIT 21

Execution time: 0.001001s [Database: default]
<QuerySet [<Paciente: Juan>]>
"""
# Consulta con or
pacientes = Paciente.objects.filter(Q(fecha_nacimiento__year=1980) | Q(tipo_sangre__tipo="O+"))
"""
In [36]: pacientes = Paciente.objects.filter(Q(fecha_nacimiento__year=1980) | Q(tipo_sangre__tipo="O+"))

In [37]: pacientes
Out[37]: SELECT "core_paciente"."id",
       "core_paciente"."nombres",
       "core_paciente"."apellidos",
       "core_paciente"."cedula",
       "core_paciente"."fecha_nacimiento",
       "core_paciente"."telefono",
       "core_paciente"."email",
       "core_paciente"."sexo",
       "core_paciente"."estado_civil",
       "core_paciente"."direccion",
       "core_paciente"."latitud",
       "core_paciente"."longitud",
       "core_paciente"."tipo_sangre_id",
       "core_paciente"."alergias",
       "core_paciente"."enfermedades_cronicas",
       "core_paciente"."medicacion_actual",
       "core_paciente"."cirugias_previas",
       "core_paciente"."antecedentes_personales",
       "core_paciente"."antecedentes_familiares"
  FROM "core_paciente"
  LEFT OUTER JOIN "core_tiposangre"
    ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
 WHERE ("core_paciente"."fecha_nacimiento" BETWEEN '1980-01-01' AND '1980-12-31' OR "core_tiposangre"."tipo" = 'O+')
 ORDER BY "core_paciente"."apellidos" ASC
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [<Paciente: Juan>, <Paciente: Juan>]>
"""
# Filtrar pacientes que nacieron en 1980 o tienen tipo de sangre O+ y no tienen alergias
pacientes = Paciente.objects.filter(
    Q(fecha_nacimiento__year=1980) | Q(tipo_sangre__tipo="O+"),
    alergias__isnull=True  # Esta condición se aplica con AND implícito
)
"""
In [38]: pacientes = Paciente.objects.filter(
    ...:     Q(fecha_nacimiento__year=1980) | Q(tipo_sangre__tipo="O+"),
    ...:     alergias__isnull=True  # Esta condición se aplica con AND implícito
    ...: )

In [39]: pacientes
Out[39]: SELECT "core_paciente"."id",
       "core_paciente"."nombres",
       "core_paciente"."apellidos",
       "core_paciente"."cedula",
       "core_paciente"."fecha_nacimiento",
       "core_paciente"."telefono",
       "core_paciente"."email",
       "core_paciente"."sexo",
       "core_paciente"."estado_civil",
       "core_paciente"."direccion",
       "core_paciente"."latitud",
       "core_paciente"."longitud",
       "core_paciente"."tipo_sangre_id",
       "core_paciente"."alergias",
       "core_paciente"."enfermedades_cronicas",
       "core_paciente"."medicacion_actual",
       "core_paciente"."cirugias_previas",
       "core_paciente"."antecedentes_personales",
       "core_paciente"."antecedentes_familiares"
  FROM "core_paciente"
  LEFT OUTER JOIN "core_tiposangre"
    ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
 WHERE (("core_paciente"."fecha_nacimiento" BETWEEN '1980-01-01' AND '1980-12-31' OR "core_tiposangre"."tipo" = 'O+') AND "core_paciente"."alergias" IS NULL)
 ORDER BY "core_paciente"."apellidos" ASC
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet []>
"""
#Obtener pacientes que no tengan tipo de sangre "AB+".
pacientes = Paciente.objects.exclude(tipo_sangre__tipo="AB+").values('apellidos','tipo_sangre__descripcion')
"""
In [40]: pacientes = Paciente.objects.exclude(tipo_sangre__tipo="AB+").values('apellidos','tipo_sangre__descripcion')

In [41]:  pacientes
Out[41]: SELECT "core_paciente"."apellidos",
       "core_tiposangre"."descripcion"
  FROM "core_paciente"
  LEFT OUTER JOIN "core_tiposangre"
    ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
 WHERE NOT ("core_tiposangre"."tipo" = 'AB+' AND "core_tiposangre"."tipo" IS NOT NULL)
 ORDER BY "core_paciente"."apellidos" ASC
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [{'apellidos': 'Bohorquez', 'tipo_sangre__descripcion': None}, {'apellidos': 'Gómez', 'tipo_sangre__descripcion': None}, {'apellidos': 'Gómez', 'tipo_sangre__descripcion': 'Tipo A'}, {'apellidos': 'Pérez', 'tipo_sangre__descripcion': 'Tipo A'}, {'apellidos': 'Pérez', 'tipo_sangre__descripcion': 'Tipo O positivo'}]>
"""
#Obtener pacientes que nacieron después de 1980 y excluir aquellos con tipo de sangre "O-".
pacientes = Paciente.objects.filter(fecha_nacimiento__year__gt=1980).exclude(tipo_sangre__tipo="O+").values('apellidos','tipo_sangre__descripcion')
"""
In [42]: pacientes = Paciente.objects.filter(fecha_nacimiento__year__gt=1980).exclude(tipo_sangre__tipo="O+").values('apellidos','tipo_sangre__descripcion')

In [43]: pacientes
Out[43]: SELECT "core_paciente"."apellidos",
       "core_tiposangre"."descripcion"
  FROM "core_paciente"
  LEFT OUTER JOIN "core_tiposangre"
    ON ("core_paciente"."tipo_sangre_id" = "core_tiposangre"."id")
 WHERE ("core_paciente"."fecha_nacimiento" > '1980-12-31' AND NOT ("core_tiposangre"."tipo" = 'O+' AND "core_tiposangre"."tipo" IS NOT NULL))
 ORDER BY "core_paciente"."apellidos" ASC
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [{'apellidos': 'Bohorquez', 'tipo_sangre__descripcion': None}, {'apellidos': 'Camino', 'tipo_sangre__descripcion': 'tipo Ab+'}, {'apellidos': 'Gómez', 'tipo_sangre__descripcion': None}, {'apellidos': 'Gómez', 'tipo_sangre__descripcion': 'Tipo A'}]>
"""
# obtener el cargo cuyo id sea igul a 1(enfermera) 
cargo_1 = Cargo.objects.get(id=1)  
"""
In [44]: cargo_1 = Cargo.objects.get(id=1)
SELECT "core_cargo"."id",
       "core_cargo"."nombre",
       "core_cargo"."descripcion"
  FROM "core_cargo"
 WHERE "core_cargo"."id" = 1
 LIMIT 21

Execution time: 0.000000s [Database: default]

In [45]: cargo_1
Out[45]: <Cargo: Enfermera>
"""
# Crear dos empleados
empleado1 = Empleado(
    nombres="Juan",
    apellidos="Pérez",
    cedula="1234567893",
    fecha_nacimiento="1990-01-01",
    cargo=cargo_1,
    sueldo=1500.00,
    direccion="Calle 1, Ciudad",
    latitud=-0.123456,
    longitud=-78.123456,
)
"""
In [47]: empleado1
Out[47]: <Empleado: Pérez>
"""
empleado2 = Empleado(
    nombres="María",
    apellidos="Gómez",
    cedula="0987654327",
    fecha_nacimiento="1985-05-15",
    cargo_id=2,
    sueldo=1600.00,
    direccion="Calle 2, Ciudad",
    latitud=-0.654321,
    longitud=-78.654321,
)
"""
In [48]: empleado2
Out[48]: <Empleado: Gómez>
"""
# Guardar en la base de datos
empleado1.save()
empleado2.save()
"""
In [49]: empleado1.save()
INSERT INTO "core_empleado" ("nombres", "apellidos", "cedula", "fecha_nacimiento", "cargo_id", "sueldo", "direccion", "latitud", "longitud", "foto")
VALUES ('Juan', 'Pérez', '1234567893', '1990-01-01', 1, '1500.00', 'Calle 1, Ciudad', -0.123456, -78.123456, '') RETURNING "core_empleado"."id"

Execution time: 0.001999s [Database: default]

In [50]: empleado2.save()
INSERT INTO "core_empleado" ("nombres", "apellidos", "cedula", "fecha_nacimiento", "cargo_id", "sueldo", "direccion", "latitud", "longitud", "foto")
VALUES ('María', 'Gómez', '0987654327', '1985-05-15', 2, '1600.00', 'Calle 2, Ciudad', -0.654321, -78.654321, '') RETURNING "core_empleado"."id"

Execution time: 0.061855s [Database: default]
"""
# muestra e nombre y el sueldo de todos los empleados
emps=Empleado.objects.values('nombres','sueldo')
"""
In [51]: emps=Empleado.objects.values('nombres','sueldo')

In [52]: emps
Out[52]: SELECT "core_empleado"."nombres",
       "core_empleado"."sueldo"
  FROM "core_empleado"
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [{'nombres': 'Ana', 'sueldo': Decimal('550.00')}, {'nombres': 'Juan', 'sueldo': Decimal('1650.00')}, {'nombres': 'María', 'sueldo': Decimal('1600.00')}, {'nombres': 'Juan', 'sueldo': Decimal('1500.00')}, {'nombres': 'María', 'sueldo': Decimal('1600.00')}]>
"""
#consulta de agregados para empleados con cargo "Enfermera"
# para contar, sumar, promediar,obtener el maximo y el minimo de los sueldos de todos los empeados. Si hay condicion dada la condicion 
#                                    cargo_id=1  
resultados = Empleado.objects.filter(cargo__descripcion__icontains="Enfermera").aggregate(
    total_sueldo=Sum('sueldo'),
    promedio_sueldo=Avg('sueldo'),
    max_sueldo=Max('sueldo'),
    min_sueldo=Min('sueldo'),
    cantidad_enfermeras=Count('id')
)
"""
In [53]: resultados = Empleado.objects.filter(cargo__descripcion__icontains="Enfermera").aggregate(
    ...:     total_sueldo=Sum('sueldo'),
    ...:     promedio_sueldo=Avg('sueldo'),
    ...:     max_sueldo=Max('sueldo'),
    ...:     min_sueldo=Min('sueldo'),
    ...:     cantidad_enfermeras=Count('id')
    ...: )
SELECT (CAST(SUM("core_empleado"."sueldo") AS NUMERIC)) AS "total_sueldo",
       (CAST(AVG("core_empleado"."sueldo") AS NUMERIC)) AS "promedio_sueldo",
       (CAST(MAX("core_empleado"."sueldo") AS NUMERIC)) AS "max_sueldo",
       (CAST(MIN("core_empleado"."sueldo") AS NUMERIC)) AS "min_sueldo",
       COUNT("core_empleado"."id") AS "cantidad_enfermeras"
  FROM "core_empleado"
 INNER JOIN "core_cargo"
    ON ("core_empleado"."cargo_id" = "core_cargo"."id")
 WHERE "core_cargo"."descripcion" LIKE '%Enfermera%' ESCAPE '\'

Execution time: 0.001000s [Database: default]

In [54]: resultados
Out[54]:
{'total_sueldo': Decimal('3700'),
 'promedio_sueldo': Decimal('1233.33333333333'),
 'max_sueldo': Decimal('1650.00000000000'),
 'min_sueldo': Decimal('550'),
 'cantidad_enfermeras': 3}
"""
# agrupar campos de una tabla
# Realizar la consulta de agregados agrupados por cargo
resultados = Empleado.objects.values('cargo__nombre').annotate(
    total_sueldo=Sum('sueldo'),
    promedio_sueldo=Avg('sueldo'),
    max_sueldo=Max('sueldo'),
    min_sueldo=Min('sueldo'),
    cantidad_empleados=Count('id')
)
"""
In [55]: resultados = Empleado.objects.values('cargo__nombre').annotate(
    ...:     total_sueldo=Sum('sueldo'),
    ...:     promedio_sueldo=Avg('sueldo'),
    ...:     max_sueldo=Max('sueldo'),
    ...:     min_sueldo=Min('sueldo'),
    ...:     cantidad_empleados=Count('id')
    ...: )

In [56]: resultados
Out[56]: SELECT "core_cargo"."nombre",
       (CAST(SUM("core_empleado"."sueldo") AS NUMERIC)) AS "total_sueldo",
       (CAST(AVG("core_empleado"."sueldo") AS NUMERIC)) AS "promedio_sueldo",
       (CAST(MAX("core_empleado"."sueldo") AS NUMERIC)) AS "max_sueldo",
       (CAST(MIN("core_empleado"."sueldo") AS NUMERIC)) AS "min_sueldo",
       COUNT("core_empleado"."id") AS "cantidad_empleados"
  FROM "core_empleado"
 INNER JOIN "core_cargo"
    ON ("core_empleado"."cargo_id" = "core_cargo"."id")
 GROUP BY "core_cargo"."nombre"
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [{'cargo__nombre': 'Asistente', 'total_sueldo': Decimal('3200'), 'promedio_sueldo': Decimal('1600'), 'max_sueldo': Decimal('1600'), 'min_sueldo': Decimal('1600'), 'cantidad_empleados': 2}, {'cargo__nombre': 'Enfermera', 'total_sueldo': Decimal('3700'), 'promedio_sueldo': Decimal('1233.33333333333'), 'max_sueldo': Decimal('1650.00000000000'), 'min_sueldo': Decimal('550'), 'cantidad_empleados': 3}]>
"""
#Realizar la consulta de agregados agrupados por cargo y sueldo
resultados = Empleado.objects.values('cargo__nombre', 'sueldo').annotate(
    cantidad_empleados=Count('id')
).order_by('cargo__nombre', 'sueldo')  # Ordenar por cargo y sueldo
"""
In [57]: resultados = Empleado.objects.values('cargo__nombre', 'sueldo').annotate(
    ...:     cantidad_empleados=Count('id')
    ...: ).order_by('cargo__nombre', 'sueldo')

In [58]: resultados
Out[58]: SELECT "core_cargo"."nombre",
       "core_empleado"."sueldo",
       COUNT("core_empleado"."id") AS "cantidad_empleados"
  FROM "core_empleado"
 INNER JOIN "core_cargo"
    ON ("core_empleado"."cargo_id" = "core_cargo"."id")
 GROUP BY "core_cargo"."nombre",
          "core_empleado"."sueldo"
 ORDER BY "core_cargo"."nombre" ASC,
          "core_empleado"."sueldo" ASC
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [{'cargo__nombre': 'Asistente', 'sueldo': Decimal('1600.00'), 'cantidad_empleados': 2}, {'cargo__nombre': 'Enfermera', 'sueldo': Decimal('550.00'), 'cantidad_empleados': 1}, {'cargo__nombre': 'Enfermera', 'sueldo': Decimal('1500.00'), 'cantidad_empleados': 1}, {'cargo__nombre': 'Enfermera', 'sueldo': Decimal('1650.00'), 'cantidad_empleados': 1}]>
"""
# Realizar la consulta de empleados y agregar el nombre del cargo como un alias sin agrupar
resultados = Empleado.objects.annotate(
    cargo_descripcion=F('cargo__nombre')  
)
"""
In [59]: resultados = Empleado.objects.annotate(
    ...:     cargo_descripcion=F('cargo__nombre')
    ...: )

In [60]: resultados
Out[60]: SELECT "core_empleado"."id",
       "core_empleado"."nombres",
       "core_empleado"."apellidos",
       "core_empleado"."cedula",
       "core_empleado"."fecha_nacimiento",
       "core_empleado"."cargo_id",
       "core_empleado"."sueldo",
       "core_empleado"."direccion",
       "core_empleado"."latitud",
       "core_empleado"."longitud",
       "core_empleado"."foto",
       "core_cargo"."nombre" AS "cargo_descripcion"
  FROM "core_empleado"
 INNER JOIN "core_cargo"
    ON ("core_empleado"."cargo_id" = "core_cargo"."id")
 LIMIT 21

Execution time: 0.000000s [Database: default]
<QuerySet [<Empleado: Cortez>, <Empleado: Pérez>, <Empleado: Gómez>, <Empleado: Pérez>, <Empleado: Gómez>]>
"""
# Actualizar los sueldos en un 10% para los empleados cuyo cargo sea "Enfermera"
Empleado.objects.filter(cargo__nombre="Enfermera").update(sueldo=F('sueldo') * 1.10,direccion='Guayaquil')
"""
In [61]: Empleado.objects.filter(cargo__nombre="Enfermera").update(sueldo=F('sueldo') * 1.10,direccion='Guayaquil')
UPDATE "core_empleado"
   SET "sueldo" = ("core_empleado"."sueldo" * 1.1),
       "direccion" = 'Guayaquil'
 WHERE "core_empleado"."id" IN (
        SELECT U0."id"
          FROM "core_empleado" U0
         INNER JOIN "core_cargo" U1
            ON (U0."cargo_id" = U1."id")
         WHERE U1."nombre" = 'Enfermera'
       )

Execution time: 0.183805s [Database: default]
Out[61]: 3
"""
cargo = Cargo.objects.get(id=3)
"""
In [62]: cargo = Cargo.objects.get(id=3)
SELECT "core_cargo"."id",
       "core_cargo"."nombre",
       "core_cargo"."descripcion"
  FROM "core_cargo"
 WHERE "core_cargo"."id" = 3
 LIMIT 21

Execution time: 0.000000s [Database: default]

In [63]: cargo
Out[63]: <Cargo: Contador>
"""
# actualiza lo deseado
cargo.descripcion="Financiero"
cargo.save() # luego se graba
"""
In [64]: cargo.descripcion="Financiero"

In [65]: cargo
Out[65]: <Cargo: Contador>

In [66]: cargo.save()
UPDATE "core_cargo"
   SET "nombre" = 'Contador',
       "descripcion" = 'Financiero'
 WHERE "core_cargo"."id" = 3

Execution time: 0.546144s [Database: default]
"""
# Eliminar los tipos de sangre cuya descripcion contenido contenga "positivo"
tipos_eliminados = TipoSangre.objects.filter(descripcion__iendswith="positivo").delete()
"""
In [67]: tipos_eliminados = TipoSangre.objects.filter(descripcion__iendswith="positivo").delete()
SELECT "core_tiposangre"."id",
       "core_tiposangre"."tipo",
       "core_tiposangre"."descripcion"
  FROM "core_tiposangre"
 WHERE "core_tiposangre"."descripcion" LIKE '%positivo' ESCAPE '\'

Execution time: 0.000000s [Database: default]
BEGIN

Execution time: 0.000000s [Database: default]
UPDATE "core_paciente"
   SET "tipo_sangre_id" = NULL
 WHERE "core_paciente"."tipo_sangre_id" IN (23, 24, 26)

Execution time: 0.001146s [Database: default]
DELETE
  FROM "core_tiposangre"
 WHERE "core_tiposangre"."id" IN (26, 24, 23)

Execution time: 0.001004s [Database: default]

In [68]: tipos_eliminados
Out[68]: (3, {'core.TipoSangre': 3})
"""
cargo = Cargo.objects.get(id=3)
cargo.delete()
"""
In [69]: cargo = Cargo.objects.get(id=3)
SELECT "core_cargo"."id",
       "core_cargo"."nombre",
       "core_cargo"."descripcion"
  FROM "core_cargo"
 WHERE "core_cargo"."id" = 3
 LIMIT 21

Execution time: 0.000000s [Database: default]

In [70]: cargo
Out[70]: <Cargo: Contador>

In [71]: cargo.delete()
SELECT "core_empleado"."id",
       "core_empleado"."nombres",
       "core_empleado"."apellidos",
       "core_empleado"."cedula",
       "core_empleado"."fecha_nacimiento",
       "core_empleado"."cargo_id",
       "core_empleado"."sueldo",
       "core_empleado"."direccion",
       "core_empleado"."latitud",
       "core_empleado"."longitud",
       "core_empleado"."foto"
  FROM "core_empleado"
 WHERE "core_empleado"."cargo_id" IN (3)

Execution time: 0.000000s [Database: default]
BEGIN

Execution time: 0.000000s [Database: default]
DELETE
  FROM "core_cargo"
 WHERE "core_cargo"."id" IN (3)

Execution time: 0.001000s [Database: default]
Out[71]: (1, {'core.Cargo': 1})
"""