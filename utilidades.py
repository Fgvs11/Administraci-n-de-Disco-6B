import os
import Validaciones as v

def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
   if os.name == "posix":
      os.system ("clear")
   elif os.name == "ce" or os.name == "nt" or os.name == "dos":
      os.system ("cls")

def imprimirDatosDeEntrada(nCilindros, peticiones, cilindroInicial):
   print('Datos de entrada:')
   print(f'Numero de cilindros: {nCilindros}')
   print(f'Peticiones: {peticiones}')
   print(f'Cilindro Inicial: {cilindroInicial}')

def imprimirMenu():
   algoritmos = ('FCFS','SSTF','SCAN','C-SCAN','LOOK','C-LOOK')
   print('Algoritmos:')
   print('Seleccione el algoritmo deseado:')
   for i in range(len(algoritmos)):
      print(f'  -[{i}]{algoritmos[i]}')
   
   return v.validar(input('Ingrese el algoritmo deseado[0-5]: '),ls = 5)

def imprimirCabezera():
   print('| Cilindro Actual | Cilindro solicitado | Tiempo de espera | Desplazamiento |')

def imprimirRenglon(cActual, cSolicitado, tEspera, desp):
   cActual = str(cActual)
   cSolicitado = str(cSolicitado)
   tEspera = str(tEspera)
   desp = str(desp)
   print(f'|{cActual.center(17)}|{cSolicitado.center(21)}|{tEspera.center(18)}|{desp.center(16)}|')