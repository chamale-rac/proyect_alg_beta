import fun_struc

# ES COMO LA CENTRAL DE TRENES EN LA QUE SE INDICA EL CAMINO A TOMAR DEPENDIENDO DE LA OPCION DENTRO DE ITERMENU() ELEJIDA


def accionar(opcion):
    if opcion == 1:
        fun_struc.modificar()
    if opcion == 2:
        fun_struc.agregar()
    if opcion == 3:
        fun_struc.mostrar()
    if opcion == 4:
        fun_struc.reportes()

# ESTA ES LA FUNCION PRINCIPAL, NO CONTIENE CICLOS SINO QUE TRABAJA RECURSIVAMENTE, EN BASTANTES FUNCIONES A LO LARGO DE LA ESTRUCTURA SE REGRESA A ESTA


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
