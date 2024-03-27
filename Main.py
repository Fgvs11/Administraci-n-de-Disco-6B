import Metodos as m
import Validaciones as v
import utilidades as u


nCilindros = v.validar(input('Ingrese el numero de Cilindros[0-199]: '))
nPeticiones = v.validar(
    input('Ingrese el numero de peticiones[1-infinito]: '), li=1, ls=0)
peticiones = []

for i in range(nPeticiones):
    peticiones.append(
        v.validar(input(f'Ingrese la peticion {i + 1}: '), ls=nCilindros))

cilindroInicial = v.validar(
    input(f'Ingrese el cilindro inicial[0-{nCilindros}]: '), ls=nCilindros)

u.borrarPantalla()
u.imprimirDatosDeEntrada(nCilindros, peticiones, cilindroInicial)
seleccion = u.imprimirMenu()

bDir = v.validarBit(input('Ingrese el bit de direccion[0-1]: '))
u.imprimirCabezera(seleccion)
if seleccion == 0:
    resultados = m.FCFS(nCilindros, peticiones, cilindroInicial)
elif seleccion == 1:
    resultados = m.SSTF(nCilindros, peticiones, cilindroInicial)
elif seleccion == 2:
    resultados = m.SCAN(nCilindros, peticiones, cilindroInicial, bDir)
elif seleccion == 3:
    resultados = m.CSCAN(nCilindros, peticiones, cilindroInicial)
elif seleccion == 4:
    resultados = m.LOOK(nCilindros, peticiones, cilindroInicial)
else:
    resultados = m.CLOOK(nCilindros, peticiones, cilindroInicial)
u.imprimirFinal()
u.imprimirResultados(resultados)
