import utilidades as u
def FCFS(nCilindros, peticiones, cilindroActual):
    sTiempoEspera =0
    tiempoEspera = 0
    desp = 0
    for cilindroSolicitado in peticiones:
        tiempoEspera += desp
        sTiempoEspera += tiempoEspera
        desp = abs(cilindroSolicitado - cilindroActual)
        u.imprimirRenglon(cilindroActual, cilindroSolicitado, tiempoEspera, desp)
        cilindroActual = cilindroSolicitado
    return [tiempoEspera + desp, sTiempoEspera / len(peticiones)]

def SSTF(nCilindros, peticiones, cilindroInicial):
    pass
def SCAN(nCilindros, peticiones, cilindroInicial):
    pass
def CSCAN(nCilindros, peticiones, cilindroInicial):
    pass



def LOOK(nCilindros, peticiones, cilindroInicial):
    peticiones.sort()
    cilindroActual = cilindroInicial
    cilindrosAbajo = []
    cilindrosArriba = []
    sTiempoEspera =0
    tiempoEspera = 0
    desp = 0

    while peticiones:
        for peticion in peticiones[:]:
            if (peticion <= cilindroInicial):
                cilindrosAbajo.append(peticion)
                peticiones.remove(peticion)
            elif (peticion > cilindroInicial):
                cilindrosArriba.append(peticion)
                peticiones.remove(peticion)

    cilindrosAbajo.sort(reverse=True)
    cilindrosOrdenados = cilindrosAbajo + cilindrosArriba

    for cilindro in cilindrosOrdenados:
        tiempoEspera += desp
        sTiempoEspera += tiempoEspera
        desp = abs(cilindro - cilindroActual)
        u.imprimirRenglon(cilindroActual, cilindro, tiempoEspera, desp)
        cilindroActual = cilindro
    return [tiempoEspera + desp, sTiempoEspera / len(cilindrosOrdenados)]


def CLOOK(nCilindros, peticiones, cilindroInicial):
    peticiones.sort()
    cilindroActual = cilindroInicial
    cilindrosAbajo = []
    cilindrosArriba = []
    sTiempoEspera =0
    tiempoEspera = 0
    desp = 0

    while peticiones:
        for peticion in peticiones[:]:
            if (peticion <= cilindroInicial):
                cilindrosAbajo.append(peticion)
                peticiones.remove(peticion)
            elif (peticion > cilindroInicial):
                cilindrosArriba.append(peticion)
                peticiones.remove(peticion)

    cilindrosAbajo.sort(reverse=True)
    cilindrosArriba.sort(reverse=True)
    cilindrosOrdenados = cilindrosAbajo + cilindrosArriba

    for cilindro in cilindrosOrdenados:
        tiempoEspera += desp
        sTiempoEspera += tiempoEspera
        desp = abs(cilindro - cilindroActual)
        u.imprimirRenglon(cilindroActual, cilindro, tiempoEspera, desp)
        cilindroActual = cilindro
    return [tiempoEspera + desp, sTiempoEspera / len(cilindrosOrdenados)]