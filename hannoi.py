
n = 4;
origen = 0;
intermedio = 1;
destino = 2;

#se pasa 0 a intermedio, se pasa 1 a destino
def hannoi(n, origen, intermedio, destino):

    if n > 0:
        hannoi(n-1, origen, intermedio, destino)
        print 'origen', n, n-1
        hannoi(n-1),intermedio,destino, origen)
        
