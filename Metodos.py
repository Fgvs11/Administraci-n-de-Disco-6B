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
    pass
def CLOOK(nCilindros, peticiones, cilindroInicial):
    pass