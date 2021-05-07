import csv
import structure

# DESPLIEGA TODO EL TEXTO DE MANERA ORDENADA EN LA CONSOLA


def desplegar(arreglo):
    texto = ''
    mayor_longitud = 0
    espacios = ''
    for e in range(len(arreglo)):
        for e2 in range(len(arreglo[e])):
            if (len(str(arreglo[e][e2]))) > mayor_longitud:
                mayor_longitud = len(str(arreglo[e][e2]))

    for e in range(len(arreglo)):
        for e2 in range(len(arreglo[e])):
            espacios = ''
            longitud = mayor_longitud - len(arreglo[e][e2]) + 3
            for e3 in range(longitud):
                espacios = espacios + ' '
            espacios = espacios + '|'
            texto = texto + str(arreglo[e][e2]) + espacios

        texto = texto + '\n'

    print(texto)

# CALCULA LA DURACION Y CUMPLIMIENTO BASADO EN LOS DATOS INGRESADOS POR EL USUARIO


def calculo_datos(d7, d8):

    d7 = d7.split(':')
    d8 = d8.split(':')

    d71 = (int(d7[0])*60)+int(d7[1])
    d81 = (int(d8[0])*60)+int(d8[1])

    dfinal = d81 - d71
    objetivo = ''
    if dfinal >= 30:
        objetivo = 'Cumplido'
    else:
        objetivo = 'Sin cumplir'
    return dfinal, objetivo

# GENERA AUTOMATICAMENTE UN MENU PARA CUANDO SE HAYA FINALIZADO UNA ACCION, LA VARIABLE QUE SE LE TRANSMITE INDICA EL CASO DEL MENU'error' o 'normal'


def salir(order):
    if order == 'error':
        print('\nREFERENCIA NO ENCONTRADA...\n\t1.Regresar a Menu\n\t2.Permanecer')
    if order == 'normal':
        print('\nOPERACION FINALIZADA...\n\t1.Regresar a Menu\n\t2.Permanecer')
    confirmacion_inter = False
    confirmacion = False
    while not confirmacion_inter:
        opcion = input('\t>> Seleccione una opcion (numero): ')
        if opcion == '1':
            print('--------------------------------------------\nREGRESANDO A MENU...')
            confirmacion = True
            confirmacion_inter = True
        elif opcion == '2':
            confirmacion = False
            confirmacion_inter = True
        else:
            print('Opcion no valida')
            print('Opciones Validas\n\t1.Regresar a Menu\n\t2.Permanecer')
    return confirmacion

# LEE CUALQUIER ARCHIVO CSV SOLO TRANSMITIENDOLE EL NOMBRE DEL ARCHIVO, DEVUELVE DOS VARIABLES, UNA STRING Y UN ARRAY CON EL CONTENIDO DE LA TABLA


def leer(name):
    archivo = open(name, encoding='utf-8')
    texto = archivo.read()
    archivo.close()

    quitarlineas = texto.split('\n')
    array = []

    for quitarcomas in quitarlineas:
        array.append(quitarcomas.split(','))

    return texto, array

# SOBREESCRIBE EL ARCHIVO CSV SOLO SE LE TRANSMITE LA STRING


def dumper(dumption):
    archivo = open('archivo.csv', 'w', encoding='utf-8')
    archivo.write(dumption)
    archivo.close()

# VERIFICA QUE UNA VARIABLE SEA ENTERA


def verificar_int(mensaje):
    todo_bien = False
    while not todo_bien:
        try:
            num_entero = int(input(mensaje))
            todo_bien = True
        except:
            print("FORMATO INCORRECTO...")
    return num_entero

# VERIFICA QUE UNA VARIABLE SEA FLOAT


def verificar_float(mensaje):
    todo_bien = False
    while not todo_bien:
        try:
            num_entero = float(input(mensaje))
            todo_bien = True
        except:
            print("FORMATO INCORRECTO...")
    return num_entero

# VERIFICA QUE UNA VARIABLE ESTE EN EL FORMATO HH:MM


def verificar_horamin(mensaje):
    formato = False
    while not formato:
        num_entero = input(mensaje)
        dividido = num_entero.split(':')
        try:
            if ((len(dividido) == 2) and (0 <= int(dividido[0])*100 <= 2400) and (0 <= int(dividido[1])*100 <= 6000)):
                formato = True
                if int(dividido[0])*100 <= 900:
                    x = dividido[0]
                    y = x[0]
                    if y != '0':
                        formato = False

                if int(dividido[1])*100 <= 900:
                    x = dividido[1]
                    y = x[0]
                    if y != '0':
                        formato = False
            if not formato:
                print("FORMATO INCORRECTO...\n*revise los intervalos*")
        except:
            print("FORMATO INCORRECTO...")
    return num_entero

# VERIFICA QUE UNA VARIABLE ESTE EN EL FORMATO DD:MM:AAAA


def verificar_fecha(mensaje):
    formato = False
    while not formato:
        num_entero = input(mensaje)
        dividido = num_entero.split('/')

        try:
            if ((len(dividido) == 3) and (0 <= int(dividido[0])*100 <= 3100) and (0 <= int(dividido[1])*100 <= 1200)) and (int(dividido[2]) == 2021):
                formato = True
                if int(dividido[0])*100 <= 900:
                    x = dividido[0]
                    y = x[0]
                    if y != '0':
                        formato = False

                if int(dividido[1])*100 <= 900:
                    x = dividido[1]
                    y = x[0]
                    if y != '0':
                        formato = False
            if not formato:
                print("FORMATO INCORRECTO...\n*revise los intervalos*")
        except:
            print("FORMATO INCORRECTO...")
    return num_entero
