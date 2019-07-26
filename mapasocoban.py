'''
   0.- personaje
   1.- cajas
   2.- metas
   3.- paredes
   4.- pasillo
   5.- caja/meta
   6.-personaje/meta
'''
mapa=[[3, 3, 3, 3, 3],
      [3, 4, 0, 4, 3],
      [3, 1, 2, 4, 3], 
      [3, 3, 3, 3, 3]]

position_col= 3
position_row= 1

def printMapa():
  for x in range(len(mapa)):
    for y in range(len(mapa[x])):
     print(mapa[x][y], end= " ")
    print()
printMapa()
while True:
  move=input('a_left,d_rigth')