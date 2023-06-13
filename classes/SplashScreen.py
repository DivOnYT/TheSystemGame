from ursina import *
from ursina.camera import *

class SplashScreen(Sprite):
    """
    Classe Permettant d'afficher un écran de lancement lors du démarrage de l'application
    """
    def __init__(self, texture=None, **kwargs):
        super().__init__(texture, **kwargs)
        camera.overlay.color = color.black
        self.__state = True
        #logo = Sprite(name='ursina_splash', parent=camera.ui, texture='ursina_logo', world_z=camera.overlay.z-1, scale=.1, color=color.clear)
        self.animate_color(color.white, duration=2, delay=1, curve=curve.out_quint_boomerang)
        camera.overlay.animate_color(color.clear, duration=1, delay=4)
        destroy(self, delay=5)

    @property
    def state(self):
        return self.__state

    def splash_input(self, key):
        destroy(self)
        camera.overlay.animate_color(color.clear, duration=.25) 

if __name__ == '__main__': # tests
    app = Ursina()
    splash = SplashScreen(name='splash_systeme_solaire', parent=camera.ui, texture="systeme_solaire_logo.png", world_z=camera.overlay.z-1, scale=.1, color=color.clear)
    app.run()