# Fonctionnalité pour appuyer sur les ellipses des planètes mais enlevé car fait baisser les fps et meilleure manière de faire 
# a été trouvée avec le clic sur l'entité directement

from ursina import *


class Ellipse(Button):
    def __init__(self, **kwargs):
        super().__init__(
      model = 'circle',
      color = color.blue,
      scale = 0.3,
      **kwargs)
    
    def on_click(self):
      print("SAlut")