def __validarRango(num,li,ls):
    if li <= num and (ls == 0 or num <= ls):
        return num
    else:
        num = input(f'Error, ingrese un numero entre el rango[{li}-{ls if ls != 0 else "infinito"}]: ')
        num = validar(num, li = li, ls = ls)
        return num

def __validarNumero(num):
    try:
        num = int(num)
        return num
    except Exception:
        num = input('Ingrese un numero entero: ')
        num = validar(num)
        return num

def validar(num, li = 0, ls = 200):
    num = __validarNumero(num)
    return __validarRango(num, li, ls)