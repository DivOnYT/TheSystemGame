from ursina import *

class Stars(Entity):
    """
    Classe permettant d'afficher les étoiles dans le fond de la représentation du système solaire
    """

    def __init__(self, **kwargs):
        from ursina.shaders import unlit_shader
        super().__init__(name='stars', model='sky_dome', texture='Textures/Stars_Map', scale=9900, shader=unlit_shader)

        for key, value in kwargs.items():
            setattr(self, key, value)


    def update(self):
        self.world_position = camera.world_position