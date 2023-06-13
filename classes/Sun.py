from ursina import *

taille = 109/9 #109 fois la terre

class Sun(Entity):
    """
    Classe permettant de créer le soleil sous différents attributs que ceux d'une planète car le soleil n'en n'est pas une
    """
    def __init__(self, master, scale,add_to_scene_entities=True,  **kwargs):
        scale = scale * taille
        super().__init__(add_to_scene_entities, model='sphere', scale=scale, origin_y=-.5, texture=load_texture('Textures/Sun.jpg'), collider='box', **kwargs)
        self.master = master

    def on_click(self):
        print("Le Soleil est la plus grande entité du système solaire")
        camera.world_position = (self.position.x, self.position.y, self.position.z)
        self.master.world_position = camera.world_position
    
    """def my_update(self):
        self.rotation_y += 50 * time.dt """