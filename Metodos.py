import utilidades as u
import Validaciones as v


def FCFS(nCilindros, peticiones, cilindroActual):
    sTiempoEspera = 0
    tiempoEspera = 0
    desp = 0
    for cilindroSolicitado in peticiones:
        tiempoEspera += desp
        sTiempoEspera += tiempoEspera
        desp = abs(cilindroSolicitado - cilindroActual)
        u.imprimirRenglon(cilindroActual, cilindroSolicitado,
                          tiempoEspera, desp)
        cilindroActual = cilindroSolicitado
    return [tiempoEspera + desp, sTiempoEspera / len(peticiones)]

def SCAN(nCilindros, peticiones, cilindroInicial, bDir):
    peticiones.sort()
    cilindroActual = cilindroInicial
    cilindrosAbajo = []
    cilindrosArriba = []
    sTiempoEspera = 0
    tiempoEspera = 0
    desp = 0
    if bDir == 0:
        while peticiones:
            for peticion in peticiones[:]:
                if (peticion <= cilindroInicial):
                    cilindrosAbajo.append(peticion)
                    peticiones.remove(peticion)
                elif (peticion > cilindroInicial):
                    cilindrosArriba.append(peticion)
                    peticiones.remove(peticion)

        cilindrosAbajo.append(0)
        cilindrosAbajo.sort(reverse=True)
        cilindrosOrdenados = cilindrosAbajo + cilindrosArriba

        for cilindro in cilindrosOrdenados:
            tiempoEspera += desp
            sTiempoEspera += tiempoEspera
            desp = abs(cilindro - cilindroActual)
            u.imprimirRenglon(cilindroActual, cilindro, tiempoEspera, desp)
            cilindroActual = cilindro
        cilindrosOrdenados.pop(0)
        return [tiempoEspera + desp, sTiempoEspera / len(cilindrosOrdenados)]

    else:
        while peticiones:
            for peticion in peticiones[:]:
                if (peticion >= cilindroInicial):
                    cilindrosArriba.append(peticion)
                    peticiones.remove(peticion)
                elif (peticion < cilindroInicial):
                    cilindrosAbajo.append(peticion)
                    peticiones.remove(peticion)

        cilindrosArriba.append(199)
        cilindrosArriba.sort()
        cilindrosAbajo.sort(reverse=True)
        cilindrosOrdenados = cilindrosArriba + cilindrosAbajo

        for cilindro in cilindrosOrdenados:
            tiempoEspera += desp
            sTiempoEspera += tiempoEspera
            desp = abs(cilindro - cilindroActual)
            u.imprimirRenglon(cilindroActual, cilindro, tiempoEspera, desp)
            cilindroActual = cilindro
        cilindrosOrdenados.pop(0)
        return [tiempoEspera + desp, sTiempoEspera / len(cilindrosOrdenados)]

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

    
def CSCAN(nCilindros, peticiones, cilindroInicial):
    peticiones.sort()
    cilindroActual = cilindroInicial
    cilindrosAbajo = []
    cilindrosArriba = []
    sTiempoEspera = 0
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

    cilindrosAbajo.append(0)
    cilindrosArriba.append(199)
    cilindrosAbajo.sort(reverse=True)
    cilindrosArriba.sort(reverse=True)
    cilindrosOrdenados = cilindrosAbajo + cilindrosArriba
    for cilindro in cilindrosOrdenados:
        tiempoEspera += desp
        sTiempoEspera += tiempoEspera
        desp = abs(cilindro - cilindroActual)
        u.imprimirRenglon(cilindroActual, cilindro, tiempoEspera, desp)
        cilindroActual = cilindro
    cilindrosOrdenados.pop(0)
    cilindrosOrdenados.pop(0)
    return [tiempoEspera + desp, sTiempoEspera / len(cilindrosOrdenados)]


def LOOK(nCilindros, peticiones, cilindroInicial):
    pass


def CLOOK(nCilindros, peticiones, cilindroInicial):
    pass
