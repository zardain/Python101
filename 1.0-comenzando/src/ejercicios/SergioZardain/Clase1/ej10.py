# -*- coding: utf-8 -*-
import random
from time import sleep
#SUPER HARD, vale 10 puntos para Griffindor: Escribir un piedra, papel o tijera de 1 ronda.
<<<<<<< HEAD

print "***** Piedra, papel o tijera (el mejor de 3 intentos) *****"
print ""
sleep(1)

#Funcion que realiza la lógica del juego

constanteIntentos=3
intentos = 1

#	1- Piedra
#	2- Papel
#	3- Tijera

#	0- Perdi con la CPU
#	1- Gané a la CPU
#	2- Empatamos

# [PIEDRA,PAPEL,TIJERA]

matrizJuego = [[2,0,1],[1,2,0],[0,1,2]]
matrizTexto = [0,"Piedra","Papel","Tijera"]

while str(intentos) != constanteIntentos:
  print "intento n°: " + str(intentos)
  print " "
# Valido que haya ingresado un número
  ingreseValor=0
  while ingreseValor == 0:
    print "¿Piedra(1), papel(2) o tijera(3)?"
    opcion = raw_input()
    if opcion.isdigit():
      ingreseValor=1
      if int(opcion) > 0 and int(opcion) < 4:
          print "...", matrizTexto[int(opcion)]
          print " "
    else:
      print "	ingrese un numero, reintente."
      print " "
      ingreseValor=0

#PC, opción al azar
  sleep(1)
  azar = random.choice([1,2,3])
  print "PC eligió...", azar,matrizTexto[azar]

#Muestro el resultado
  if matrizJuego[int(opcion)][int(azar)] == 0:
	print "Perdiste."
  elif matrizJuego[int(opcion)][int(azar)] == 1:
	print "Ganaste!"
  else:
	print "Empate..."
  sleep(1)
  print ""
  intentos += 1
print "PARTIDA TERMINADA"
=======
#http://www.pythondiario.com/2013/11/piedra-papel-o-tijera-juego-en-python.html
import random
from time import sleep

print "****** Piedra, papel o tijera (3 intentos) ******"
print ""
sleep(2)

# Inicio
 x = 0
 tu = 0
 pc = 0
 
 while str(x) != 3:
  
  ingresoOpcion = false
  while ingresoOpcion == false
    print "Piedra (1), papel (2) o tijera (3)?"
    opcion = raw_input()
    if opcion != 1 and opcion != 2 and opcion != 3:
        ingresoOpcion = false
    else:
        ingresoOpcion = true
    
  
  
  
  azar = random.choice(["piedra", "papel", "tijera"])
  if opcion == azar:
   print "El pc tambien elijio", azar
   print ""
  elif azar == "tijera" and opcion == "papel":
   x += 1
   pc += 1
   print "El PC saco", azar
   print "Tu", tu, "PC", pc
   print ""
  elif azar == "tijera" and opcion == "piedra":
   x += 1
   tu += 1
   print "El PC saco", azar
   print "Tu", tu, "PC", pc
   print ""
  elif azar == "piedra" and opcion == "tijera":
   x += 1
   pc += 1
   print "El PC saco", azar
   print "Tu", tu, "PC", pc
   print ""
  elif azar == "piedra" and opcion == "papel":
   x += 1
   tu += 1
   print "El PC saco", azar
   print "Tu", tu, "PC", pc
   print ""
  elif azar == "papel" and opcion == "tijera":
   x += 1
   tu += 1
   print "El PC saco", azar
   print "Tu", tu, "PC", pc
   print ""
  elif azar == "papel" and opcion == "piedra":
   x += 1
   pc += 1
   print "El pc saco", azar
   print "Tu", tu, "PC", pc
   print ""
  else:
   print "Opcion incorrecta, vuleva a intentarlo"
 
 print ""
 
 if pc > tu:
  print "Gano el PC", pc, "a", tu
 elif pc == tu:
  print "Empataron", tu, "a", pc
 else:
  print "Ganaste", tu, "a", pc
 
 print ""
 print "PARTIDA TERMINADA"
>>>>>>> a8aa2570488521924969709016c82269199a5c9b
