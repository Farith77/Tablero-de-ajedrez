from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return vertical

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    length = len(self.img[0])
    horizontal = []

    for r in self.img:
      row = ""
      x = 0
      while x < length:
        row += r[length -1 -x]
        x += 1
      horizontal.append(row)

    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negativo = []

    for r in self.img:
      x = 0
      row = ""
      while x < len(r):
        row += self._invColor(r[x])
        x += 1
      negativo.append(row)
    return Picture(negativo)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    derecho = []
    x = 0
    while x < len(self.img):
      derecho.append(self.img[x] + p.img[x])
      x += 1

    return Picture(derecho)


  def up(self, p):
    arriba = []
    for r in self.img:
      arriba.append(r)

    for r in p.img:
      arriba.append(r)
    return Picture(arriba)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    abajo = []
    for r in p.img:
      abajo.append(r)

    for r in self.img:
      abajo.append(r)

    return Picture(abajo)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    horizontal = []

    for r in self.img:
      x = 1
      row = ""
      while x <= n:
        row += r
        x += 1
      horizontal.append(row)

    return Picture(horizontal)

  def verticalRepeat(self, n):
    vertical = []

    x = 1
    while x <= n:
      for r in self.img:
        vertical.append(r)
      x += 1

    return Picture(vertical)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    rotada = []
    i = 0
    while (i < len(self.img[0])):
      row = ""
      j = len(self.img) - 1
      while (j >= 0):
        aux = self.img[j]
        row += aux[i]
        j -= 1
      rotada.append(row)
      i += 1
      
    return Picture(rotada)

  def behind(self, p):
    behindColor = p.img[0][0]
    newimg = []
    for r in self.img:
      x = 0
      row = ""
      while x < len(r): 
        if r[x] == " ":
          row += behindColor
        else:
          row += r[x]
        x += 1
      newimg.append(row)

    return Picture(newimg)
