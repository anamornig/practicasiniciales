def anio_bisiesto(anio):
    if type(anio) !=int:
        print('Error: ingrese un numero')
        return 
    if (anio%4==0 and anio%100 !=0 or anio %400 ==0):
        print('El año es bisiesto')
    else:
        print('El año no es bisiesto')

anio = 2004
anio_bisiesto(anio)