'''
   0=personaje
   1=cajas
   2=paredes
   3=metas
   4=pasillo
   5=cajas/metas
'''
mapa=[[2,2,2,2,2,2,2],
      [2,4,4,0,4,4,2],
      [2,4,4,4,4,4,2],
      [2,2,2,2,2,2,2],]
for x in range(len(mapa)):
    for y in range (len(mapa[x])):
        print(mapa[x][y], end=" " )
    
    print("")