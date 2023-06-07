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
    horizontal =[]
    for value in self.img:
        horizontal.append(value[::-1])
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negativo_imagen = []
    for row in self.img:
        negativo_row = [self._invColor(pixel) for pixel in row]
        negativo_imagen.append(negativo_row)
    return Picture(negativo_imagen)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    joinRigth = []
    i = 0
    while i < len(self.img):
        joinRigth.append(self.img[i] + p.img[i])
        i++;
    return Picture(joinRigth)

  def up(self, p):
    new_img = p.img + self.img
    return Picture(new_img)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    if actual == "":
        return p
    else:
        return self
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    repeated_figure = self * n
    return Picture(repeated_figure)

  def verticalRepeat(self, n):
    repeated_figure = self + "\n" + (self + "\n") * (n - 1)
    return Picture(repeated_figure)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    rotated_figure = ""
    lines = actual.split("\n")
    max_length = max(len(line) for line in lines)
    for i in range(max_length):
        for j in range(len(lines)-1, -1, -1):
            if i < len(lines[j]):
                rotated_figure += lines[j][i]
            else:
                rotated_figure += " "
        rotated_figure += "\n"
    return Picture(rotated_figure.strip())

