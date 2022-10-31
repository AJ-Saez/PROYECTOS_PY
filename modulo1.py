print("algoritmo isla del tesoro")
print("bienvenido a la isla tu mision sera encontrar el tesoro")
camino=input("hay dos caminos puedes elegir('derecha o bajar')¿cual eliges?:")
if camino=="derecha":
    print("te atacaron unos monos GAME OVER'")
elif camino=="bajar" :
    print("te encuentras en lago")
    lago=input("¿saltas o nadas?:")
    if lago=="nadas":
        print("te comieron las pirañas 'GAME OVER'") 
    elif lago=="saltas" :
        print("te encuentras con 4 puertas,¿cual eliges la Negra, la blanca, la gris, o la verde?:")
        puertas=input("elige la puerta que seleccionaste:  ")
        if puertas=="negra" :
           print("caiste en un volcan 'GAME OVER'")
        elif puertas=="blanca" :
           print("caiste en arenas movedizas 'GAME OVER':") 
        elif puertas=="gris" :
           print("te muerde una serpiente 'GAME OVER'")    
        elif puertas=="verde" :
           print("conseguiste el tesoro Ganaste un trofeo")  