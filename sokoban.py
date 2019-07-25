'''
    0- Personaje
    1- Caja
    2- Paredes 
    3- Metas
    4- Pasillo
    5- Caja/Meta
'''
mapa=[2, 4, 4, 4, 0, 4, 4, 1, 3, 2]  
print (mapa)
position_x=4
while True:
    print (mapa)
    move = input("D.right , A.left")
    tem_x=position_x
    if move =='D'and mapa [position_x+1]!=2:
        position_x = position_x + 1
    elif move == 'A':
        position_x = position_x - 1
    mapa[tem_x]=4
    mapa[position_x]=0

	 