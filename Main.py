import Metodos as m
import Validaciones as v
import utilidades as u


nCilindros = v.validar(input('Ingrese el numero de Cilindros[0-200]: '))
nPeticiones = v.validar(input('Ingrese el numero de peticiones[1-infinito]: '), li = 1, ls = 0)
peticiones = []

for i in range(nPeticiones):
    peticiones.append(v.validar(input(f'Ingrese la peticion {i + 1}: ')))

cilindroInicial = v.validar(input('Ingrese el cilindro inicial[0-200]: '))

u.borrarPantalla()
u.imprimirDatosDeEntrada(nCilindros, peticiones, cilindroInicial)
seleccion = u.imprimirMenu()

u.imprimirCabezera()
if seleccion == 0:
    m.FCFS(nCilindros, peticiones, cilindroInicial)
elif seleccion == 1:
    m.SSTF(nCilindros, peticiones, cilindroInicial)
elif seleccion == 2:
    m.SCAN(nCilindros, peticiones, cilindroInicial)
elif seleccion == 3:
    m.CSCAN(nCilindros, peticiones, cilindroInicial)
elif seleccion == 4:
    m.LOOK(nCilindros, peticiones, cilindroInicial)
else:
    m.CLOOK(nCilindros, peticiones, cilindroInicial)





