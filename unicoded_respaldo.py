'''
Este es archivo de RESPALDO en caso la version modularizada del programa presente problemas. 
En este archivo esta el programa entero, lo adjuto pues la separacion en modulos la hice en poco tiempo, pues estaba indeciso en cual era la mejor
forma para presentar el reto y pues mejor decidi presentarla de ambas maneras. 
'''
# ESTE ARCHIVO NO ESTA COMENTADO, SIN EMBARGO SE UTILIZAN LAS MISMAS FUNCIONES QUE EN EL MODULAR, POR LO QUE PUEDE ENCONTRAR COMENTARIOS EN ESA VERSION
#####Imports#####
import csv
#################

#####Funciones#####
#####Operacion#####


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


def leer(name):
    archivo = open(name, encoding='utf-8')
    texto = archivo.read()
    archivo.close()

    quitarlineas = texto.split('\n')
    array = []

    for quitarcomas in quitarlineas:
        array.append(quitarcomas.split(','))

    return texto, array


def dumper(dumption):
    archivo = open('archivo.csv', 'w', encoding='utf-8')
    archivo.write(dumption)
    archivo.close()


def verificar_int(mensaje):
    todo_bien = False
    while not todo_bien:
        try:
            num_entero = int(input(mensaje))
            todo_bien = True
        except:
            print("FORMATO INCORRECTO...")
    return num_entero


def verificar_float(mensaje):
    todo_bien = False
    while not todo_bien:
        try:
            num_entero = float(input(mensaje))
            todo_bien = True
        except:
            print("FORMATO INCORRECTO...")
    return num_entero


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


###################

#####Funciones#####
#####Estructural####


def modificar():
    confirmacion = False
    while not confirmacion:
        print('--------------------------------------------\nEDITANDO...')
        normal, arreglo = leer('archivo.csv')
        parametro_1 = input('\t>> Ingresar nombre para busqueda: ')
        parametro_0 = verificar_fecha('\t>> Ingresar fecha para busqueda: ')
        for e in range(len(arreglo)):
            if (parametro_1 == arreglo[e][1]) and (parametro_0 == arreglo[e][0]):
                tochange = e
                confirmacion = True
        if confirmacion:
            d = []

            print('\nREFERENCIA ENCONTRADA...')

            repetido = 1

            while repetido != 0:
                repetido = 0
                c = True
                edit = False
                while c:
                    continuar = verificar_int(
                        '\t¿Desea editar Fecha y Nombre?\n\t\t1. Si\n\t\t2. No\n\t>> Seleccione una opción (numero): ')
                    if continuar == 1:
                        dato1 = verificar_fecha(
                            '\t>> Fecha(dd/mm/aaaa) *Unico año permitido 2021*: ')
                        dato0 = input('\t>> Nombre(texto): ')
                        c = False
                        edit = True
                    elif continuar == 2:
                        dato0 = ''
                        dato1 = ''
                        c = False
                        d.append(arreglo[e][0])
                        d.append(arreglo[e][1])
                    else:
                        print('OPCION INVALIDA...')

                for e in range(len(arreglo)):
                    if (dato1 == arreglo[e][1]) and (dato0 == arreglo[e][0]) and (edit == True):
                        repetido = repetido + 1
                if repetido > 0:
                    print(
                        'Esta fecha y nombre ya se encuentran el la base de datos, \nsolo puede haber un registro por usuario al en la misma fecha.\nIntente de nuevo...')
                if (repetido == 0) and (edit == True):
                    d.append(dato1)
                    d.append(dato0)
            c = True
            while c:
                continuar = verificar_int(
                    '\n\t¿Desea editar Edad?\n\t\t1. Si\n\t\t2. No\n\t>> Seleccione una opción (numero): ')
                if continuar == 1:
                    d.append(verificar_int('\t>> Edad(entero): '))
                    c = False
                elif continuar == 2:
                    d.append(arreglo[e][2])
                    c = False
                else:
                    print('OPCION INVALIDA...')

            c = True
            while c:
                continuar = verificar_int(
                    '\n\t¿Desea editar Peso?\n\t\t1. Si\n\t\t2. No\n\t>> Seleccione una opción (numero): ')
                if continuar == 1:
                    d.append(verificar_float('\t>> Peso(decimales): '))
                    c = False
                elif continuar == 2:
                    d.append(arreglo[e][3])
                    c = False
                else:
                    print('OPCION INVALIDA...')

            c = True
            while c:
                continuar = verificar_int(
                    '\n\t¿Desea editar Altura?\n\t\t1. Si\n\t\t2. No\n\t>> Seleccione una opción (numero): ')
                if continuar == 1:
                    d.append(verificar_float('\t>> Altura(decimales): '))
                    c = False
                elif continuar == 2:
                    d.append(arreglo[e][4])
                    c = False

                else:
                    print('OPCION INVALIDA...')

            c = True
            while c:
                continuar = verificar_int(
                    '\n\t¿Desea editar Hora inicio y Hora fin?\n\t\t1. Si\n\t\t2. No\n\t>> Seleccione una opción (numero): ')
                if continuar == 1:
                    d.append(verificar_horamin('\t>> Hora Inicio(hh:mm): '))
                    d.append(verificar_horamin('\t>> Hora Fin(hh:mm): '))

                    dato7, dato8 = calculo_datos(d[5], d[6])

                    d.append(dato7)
                    d.append(dato8)
                    c = False
                elif continuar == 2:
                    d.append(arreglo[e][5])
                    d.append(arreglo[e][6])
                    d.append(arreglo[e][7])
                    d.append(arreglo[e][8])
                    c = False
                else:
                    print('OPCION INVALIDA...')

            texto = ''
            for e in range(len(d)):
                arreglo[tochange][e] = str(d[e])
            for e in range(len(arreglo)):
                textotemp = ','.join(arreglo[e])
                if e < (len(arreglo)-1):
                    texto += textotemp + '\n'
                if e == (len(arreglo)-1):
                    texto += textotemp
            dumper(texto)
            w = 0
        if not confirmacion:
            confirmacion = salir('error')
            w = 1
        if confirmacion and w == 0:
            confirmacion = salir('normal')

    itermenu()


def agregar():
    confirmacion = False
    while not confirmacion:
        normal, arreglo = leer('archivo.csv')
        d = []
        print('--------------------------------------------\nINGRESANDO DATOS...')
        d.append(verificar_fecha(
            '\t>> Fecha(dd/mm/aaaa) *Unico año permitido 2021*: '))
        d.append(input('\t>> Nombre(texto): '))
        confirmacion_inter = False
        for e in range(len(arreglo)):
            if (d[1] == arreglo[e][1]) and (d[0] == arreglo[e][0]):
                confirmacion_inter = True
        if not confirmacion_inter:
            d.append(verificar_int('\t>> Edad(entero): '))
            d.append(verificar_float('\t>> Peso(decimales): '))
            d.append(verificar_float('\t>> Altura(decimales): '))
            d.append(verificar_horamin('\t>> Hora Inicio(hh:mm): '))
            d.append(verificar_horamin('\t>> Hora Fin(hh:mm): '))

            dato7, dato8 = calculo_datos(d[5], d[6])

            d.append(dato7)
            d.append(dato8)
            texto = ''
            for e in range(len(d)):
                d[e] = str(d[e])
            arreglo.append(d)

            for e in range(len(arreglo)):
                textotemp = ','.join(arreglo[e])
                if e < (len(arreglo)-1):
                    texto += textotemp + '\n'
                if e == (len(arreglo)-1):
                    texto += textotemp

            dumper(texto)

            confirmacion = salir('normal')
        if confirmacion_inter:
            print(
                '*no es permitido ingresar dos registros usuario en la misma fecha')
            confirmacion = salir('error')

    itermenu()


def mostrar():
    confirmacion = False
    while not confirmacion:
        print('--------------------------------------------\nMOSTRANDO DATOS...\n')
        normal, arreglo = leer('archivo.csv')
        desplegar(arreglo)

        confirmacion = salir('normal')
    itermenu()


def reportes():
    confirmacion = False
    while not confirmacion:
        print('--------------------------------------------\nMOSTRANDO REPORTES...')
        normal, arreglo = leer('archivo.csv')
        x = 0
        n = ''
        multiples = False

        for e in range(1, len(arreglo)):
            if x == int(arreglo[e][7]):
                n = n + ',' + arreglo[e][1]
                multiples = True

            if x < int(arreglo[e][7]):
                x = int(arreglo[e][7])
                n = arreglo[e][1]
                multiples = False

        if multiples:
            print('\n\t- Los usuarios con la sesión mas larga son',
                  n, 'con una sesión de', x, 'minutos')
        if not multiples:
            print('\n\t- El usuario con la sesión mas larga es',
                  n, 'con una sesión de', x, 'minutos.')
        almacen = {}
        for e in range(1, len(arreglo)):
            try:
                almacen[arreglo[e][1]] = almacen[arreglo[e][1]] + 1
            except:
                almacen[arreglo[e][1]] = 1

        sor = dict(sorted(almacen.items(), key=lambda item: item[1]))
        sor_inverted = list(reversed(sor))

        mayor = sor_inverted[0]
        text = mayor
        multiples = False
        for e in range(1, len(sor_inverted)):
            if sor[mayor] == sor[sor_inverted[e]]:
                text = text + ',' + sor_inverted[e]
                multiples = True
            if sor[mayor] < sor[sor_inverted[e]]:
                text = sor_inverted[e]
                multiples = False
        if multiples:
            print('\t- Los usuarios con mayor numero de registros son',
                  text, 'con', sor[mayor], 'registros')
        if not multiples:
            print('\t- El usuario con mayor numero de registros es',
                  text, 'con', sor[mayor], 'registros')

        confirmacion = salir('normal')

    itermenu()


def accionar(opcion):
    if opcion == 1:
        modificar()
    if opcion == 2:
        agregar()
    if opcion == 3:
        mostrar()
    if opcion == 4:
        reportes()


def itermenu():
    menu = '--------------------------------------------\n\tMENU\n\n1. Editar registros\n2. Agregar registros\n3. Mostrar registros\n4. Imprimir reportes\n5. Salir\n'

    print(menu)
    opcion = input('\t>> Seleccione una opción (numero): ')
    if (opcion == '1') or (opcion == '2') or (opcion == '3') or (opcion == '4'):
        accionar(int(opcion))
    elif opcion == '5':
        print('bye')
    else:
        print('--------------------------------------------\nOPCION INVALIDA...')
        itermenu()
###################


#####Starter#####
itermenu()
#################
