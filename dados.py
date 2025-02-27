import random


pool = []
hand = []
PuntosTemporal=0


class jugador:
    
    def __init__(self, nombre):
        self.tiradas=6
        self.puntuacion = 0
        self.nombre = nombre


def puntuar(lista):
    puntillos = 0
    for elemento in lista:
        if elemento == 1:
            puntillos+=100
        elif elemento == 5:
            puntillos+=50
    return puntillos


def dadeando(self,PuntosTemporal, pool, hand):
    pool.clear()
    hand.clear()
    self.tiradas = 6
    print(f"Le toca a {self.nombre}")
    print("Dados en la mesa")
    for i in range(self.tiradas):
        dado = random.randint(1,6)
        print(f"{i}: {dado}")
        pool.append(int(dado))
    salir = False
    while salir == False:
        print(f"Dados en la mano\n{hand}")
        print("Qué dado quieres coger?(por orden de aparicion)")
        opcion = input("(q para puntuar y pasar)| (f para puntuar y seguir)")
        
        match opcion:
            case "0":
                hand.append(pool[0])
                pool.remove(pool[0])
                cont=0
                for i in pool:
                    print(f"{cont}: {i}")
                    cont+=1
                self.tiradas-=1
            case "1":
                hand.append(pool[1])
                pool.remove(pool[1])
                cont=0
                for i in pool:
                    print(f"{cont}: {i}")
                    cont+=1
                self.tiradas-=1
            case "2":
                hand.append(pool[2])
                pool.remove(pool[2])
                cont=0
                for i in pool:
                    print(f"{cont}: {i}")
                    cont+=1
                self.tiradas-=1
            case "3":
                hand.append(pool[3])
                pool.remove(pool[3])
                cont=0
                for i in pool:
                    print(f"{cont}: {i}")
                    cont+=1
                self.tiradas-=1
            case "4":
                hand.append(pool[4])
                pool.remove(pool[4])
                cont=0
                for i in pool:
                    print(f"{cont}: {i}")
                    cont+=1
                self.tiradas-=1
            case "5":
                hand.append(pool[5])
                pool.remove(pool[5])
                cont=0
                for i in pool:
                    print(f"{cont}: {i}")
                    cont+=1
                self.tiradas-=1
            case "6":
                hand.append(pool[6])
                pool.remove(pool[6])
                cont=0
                for i in pool:
                    print(f"{cont}: {i}")
                    cont+=1
                self.tiradas-=1
            case "q":
                PuntosTemporal += puntuar(hand)
                self.puntuacion+=PuntosTemporal
                salir=True
                print(f"Tienes {self.puntuacion} puntos")
            case "f":
                PuntosTemporal += puntuar(hand)
                try:
                    pool.count(int)
                except ValueError:
                    self.tiradas=6
                pool.clear()
                hand.clear()
                print(f"Llevas {PuntosTemporal} puntos")
                for i in range(self.tiradas):
                    dado = random.randint(1,6)
                    print(f"{i}: {dado}")
                    pool.append(int(dado))


nombre1 = input("Nombre del jugador 1\n")
nombre2 = input("Nombre del jugador 2\n")

ruben = jugador(nombre1)
otro = jugador(nombre2)
while ruben.puntuacion or otro.puntuacion < 4000:
    dadeando(ruben,PuntosTemporal , pool, hand)
    dadeando(otro, PuntosTemporal, pool, hand)