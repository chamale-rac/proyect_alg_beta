import fun_opera
import structure

# FUNCION CON LA QUE SE MODIFICA UN ARCHIVO, EN ESTA SE SOLICITAN LOS DATOS Y SE EVALUA


def modificar():
    confirmacion = False
    while not confirmacion:
        print('--------------------------------------------\nEDITANDO...')
        normal, arreglo = fun_opera.leer('archivo.csv')
        parametro_1 = input('\t>> Ingresar nombre para busqueda: ')
        parametro_0 = fun_opera.verificar_fecha(
            '\t>> Ingresar fecha para busqueda: ')
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
                    continuar = fun_opera.verificar_int(
                        '\t¿Desea editar Fecha y Nombre?\n\t\t1. Si\n\t\t2. No\n\t>> Seleccione una opción (numero): ')
                    if continuar == 1:
                        dato1 = fun_opera.verificar_fecha(
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
                continuar = fun_opera.verificar_int(
                    '\n\t¿Desea editar Edad?\n\t\t1. Si\n\t\t2. No\n\t>> Seleccione una opción (numero): ')
                if continuar == 1:
                    d.append(fun_opera.verificar_int('\t>> Edad(entero): '))
                    c = False
                elif continuar == 2:
                    d.append(arreglo[e][2])
                    c = False
                else:
                    print('OPCION INVALIDA...')

            c = True
            while c:
                continuar = fun_opera.verificar_int(
                    '\n\t¿Desea editar Peso?\n\t\t1. Si\n\t\t2. No\n\t>> Seleccione una opción (numero): ')
                if continuar == 1:
                    d.append(fun_opera.verificar_float(
                        '\t>> Peso(decimales): '))
                    c = False
                elif continuar == 2:
                    d.append(arreglo[e][3])
                    c = False
                else:
                    print('OPCION INVALIDA...')

            c = True
            while c:
                continuar = fun_opera.verificar_int(
                    '\n\t¿Desea editar Altura?\n\t\t1. Si\n\t\t2. No\n\t>> Seleccione una opción (numero): ')
                if continuar == 1:
                    d.append(fun_opera.verificar_float(
                        '\t>> Altura(decimales): '))
                    c = False
                elif continuar == 2:
                    d.append(arreglo[e][4])
                    c = False

                else:
                    print('OPCION INVALIDA...')

            c = True
            while c:
                continuar = fun_opera.verificar_int(
                    '\n\t¿Desea editar Hora inicio y Hora fin?\n\t\t1. Si\n\t\t2. No\n\t>> Seleccione una opción (numero): ')
                if continuar == 1:
                    d.append(fun_opera.verificar_horamin(
                        '\t>> Hora Inicio(hh:mm): '))
                    d.append(fun_opera.verificar_horamin(
                        '\t>> Hora Fin(hh:mm): '))

                    dato7, dato8 = fun_opera.calculo_datos(d[5], d[6])

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
            fun_opera.dumper(texto)
            w = 0
        if not confirmacion:
            confirmacion = fun_opera.salir('error')
            w = 1
        if confirmacion and w == 0:
            confirmacion = fun_opera.salir('normal')
    structure.itermenu()

# FUNCION PARA AGREGAR DATOS, EN ESTA SE SOLICITAN LOS DATOS Y SE EVALUA


def agregar():
    confirmacion = False
    while not confirmacion:
        normal, arreglo = fun_opera.leer('archivo.csv')
        d = []
        print('--------------------------------------------\nINGRESANDO DATOS...')
        d.append(fun_opera.verificar_fecha(
            '\t>> Fecha(dd/mm/aaaa) *Unico año permitido 2021*: '))
        d.append(input('\t>> Nombre(texto): '))
        confirmacion_inter = False
        for e in range(len(arreglo)):
            if (d[1] == arreglo[e][1]) and (d[0] == arreglo[e][0]):
                confirmacion_inter = True
        if not confirmacion_inter:
            d.append(fun_opera.verificar_int('\t>> Edad(entero): '))
            d.append(fun_opera.verificar_float('\t>> Peso(decimales): '))
            d.append(fun_opera.verificar_float('\t>> Altura(decimales): '))
            d.append(fun_opera.verificar_horamin('\t>> Hora Inicio(hh:mm): '))
            d.append(fun_opera.verificar_horamin('\t>> Hora Fin(hh:mm): '))

            dato7, dato8 = fun_opera.calculo_datos(d[5], d[6])

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

            fun_opera.dumper(texto)

            confirmacion = fun_opera.salir('normal')
        if confirmacion_inter:
            print(
                '*no es permitido ingresar dos registros usuario en la misma fecha')
            confirmacion = fun_opera.salir('error')

    structure.itermenu()

# FUNCION PARA MOSTRAR DATOS


def mostrar():
    confirmacion = False
    while not confirmacion:
        print('--------------------------------------------\nMOSTRANDO DATOS...\n')
        normal, arreglo = fun_opera.leer('archivo.csv')
        fun_opera.desplegar(arreglo)

        confirmacion = fun_opera.salir('normal')
    structure.itermenu()

# FUNCION PARA CALCULAR LOS REPORTES BASADOS EN LOS DATOS DE LA TABLA


def reportes():
    confirmacion = False
    while not confirmacion:
        print('--------------------------------------------\nMOSTRANDO REPORTES...')
        normal, arreglo = fun_opera.leer('archivo.csv')
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

        confirmacion = fun_opera.salir('normal')

    structure.itermenu()
