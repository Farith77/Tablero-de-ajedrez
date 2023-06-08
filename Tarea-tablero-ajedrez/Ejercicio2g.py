from interpreter import draw
from chessPictures import *

#Agregando fichas
torreNegra1 = rock.negative().behind(square)
caballoNegro1 = knight.negative().behind(square.negative())
alfilNegro1 = bishop.negative().behind(square)
reynaNegra = queen.negative().behind(square.negative())
reyNegro = king.negative().behind(square)
alfilNegro2 = bishop.negative().behind(square.negative())
caballoNegro2 = knight.negative().behind(square)
torreNegra2 = rock.negative().behind(square.negative())
#agregando filas
fila1 = torreNegra1.join(caballoNegro1).join(alfilNegro1).join(reynaNegra).join(reyNegro).join(alfilNegro2).join(caballoNegro2).join(torreNegra2)
fila2 = pawn.negative().behind(square.negative()).join(pawn.negative().behind(square)).horizontalRepeat(4)

fila3 = square.join(square.negative()).horizontalRepeat(4)
fila4 = fila3.negative()
fila5 = fila3
fila6 = fila4

fila7 = fila2.negative()
fila8 = fila1.negative()

draw(fila1.up(fila2).up(fila3).up(fila4).up(fila5).up(fila6).up(fila7.up(fila8)))
