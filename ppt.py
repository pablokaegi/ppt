
jugador1=input("Hola jugador 1 ¿Qué eliges piedra, papel o tijeras?  ")
jugador2=input("Hola jugador 2 ¿Qué eliges piedra, papel o tijeras?  ")

condicion1=jugador1== "piedra" and jugador2== "tijeras"
condicion2=jugador1== "papel" and jugador2=="piedra"
condicion3=jugador1== "tijeras" and jugador2=="papel"

if jugador1 == jugador2:
    print("ha sido un empate")
elif condicion1 or condicion2 or condicion3 :
    print ("ha ganado el jugador 1")
else:
    print("ha ganado el jugador 2")