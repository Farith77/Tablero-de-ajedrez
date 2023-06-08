from interpreter import draw
from chessPictures import *

fila1 = square.join(square.negative()).horizontalRepeat(4)
fila2 = fila1.negative()
fila3 = fila1
fila4 = fila2

draw(fila1.up(fila2.up(fila3.up(fila4)))) 