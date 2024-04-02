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

def SSTF(nCilindros, peticiones, cilindroActual):
    peticionesCopia = peticiones[:]
    sTiempoEspera = 0
    tiempoEspera = 0
    num_peticiones = len(peticiones)  # Número total de peticiones

    for _ in range(num_peticiones):
        minDistancia = float('inf')
        siguienteCilindro = None
        for cilindroSolicitado in peticionesCopia:
            distancia = abs(cilindroSolicitado - cilindroActual)
            if distancia < minDistancia:
                minDistancia = distancia
                siguienteCilindro = cilindroSolicitado
        u.imprimirRenglon(cilindroActual, siguienteCilindro, tiempoEspera, minDistancia)
        sTiempoEspera += tiempoEspera
        tiempoEspera += minDistancia
        cilindroActual = siguienteCilindro
        peticionesCopia.remove(siguienteCilindro)  # Eliminar la petición atendida

    if num_peticiones > 0:  # Verificar si hay peticiones iniciales
        promedio_tiempo_espera = sTiempoEspera / len(peticiones)
    else:
        promedio_tiempo_espera = 0  # Asignar cero si no hay peticiones iniciales

    return [tiempoEspera, promedio_tiempo_espera]

    
def SCAN(nCilindros, peticiones, cilindroInicial):
    pass
def CSCAN(nCilindros, peticiones, cilindroInicial):
    pass
def LOOK(nCilindros, peticiones, cilindroInicial):
    pass
def CLOOK(nCilindros, peticiones, cilindroInicial):
    pass