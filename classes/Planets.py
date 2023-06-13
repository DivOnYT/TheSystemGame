#importation des modules utilisés
from ursina import *
from math import *

#from classes.Ellipses import * # old module pas utilisé

# Saturn, Mars, Earth, Mercure, Venus, Uranus, Jupiter, Neptune
# sites utilisés pour les informations : wikipedia.fr et https://www.numerama.com/sciences/1114022-quelle-planete-tourne-le-plus-vite-autour-du-soleil.html
# rayons : https://www.le-systeme-solaire.net/taille-des-planetes-du-systeme-solaire.html
# textures utilisées -> https://www.solarsystemscope.com/textures/

#Infos récoltées sur les planètes pour la programmation du modèle
# ----------------------------------------------------------------------------------------------------------------------------------------
planets = ["Saturne", "Mars", "Terre", "Mercure", "Venus", "Jupiter", "Uranus", "Neptune"]
speeds = [34848, 86868, 107320, 172332, 126072, 47052, 24516, 19548]  # vitesse de rotation par rapport au soleil en km/h
vitesseRotations = [34821, 868.220, 167.364, 10.892, 6.52, 47051, 9320, 9660] # vitesse de rotation sur la planete même en km/h
ellipse_rayons = [1_426_700_000, 227_944_000, 149_597_887.5, 57_909_050, 108_209_500, 778_340_000, 2_870_700_000, 4_498_400_000] # le rayon de l'ellipse entre le soleil et la planète en km 
rayon_planets = [58232, 3390, 6371, 2440, 6052, 69911, 25362, 24622] # rayon de la planète en km
textures_planets = ["saturn.jpg", "Mars.png", "Earth", "mercure.jpg", "Venus.jpg", "jupiter.jpg", "uranus.jpg", "neptune.jpg"]
taille = [9.14, 0.53, 1, 0.38, 0.95, 11, 3.99, 3.87] #en prenant la terre comme base, terre = 1
# ----------------------------------------------------------------------------------------------------------------------------------------

#Programmation en POO avec la classe principale : Planet()
class Planet(Entity):
    def __init__(self, model, texture, scale, collider, vitesse_rotation: int, speed:int, add_to_scene_entities=True, master=None,**kwargs):
        """
        PARAMETERS : ******
            model : modele .obj 3D
            texture : texture du modele .obj 3D en .png ou .jpg
            scale : taille de l'obj
            collider : type de collision 'box', 'sphere', 'rectangle'
            vitesse_rotation : la vitesse de rotation par rapport a la planete
            speed : vitesse de rotation par rapport au soleil
            master : la classe créatrice de l'instance
            **kwargs : tous les autre paramètres pouvant être utilisés sur une Entity
        """
        super().__init__(add_to_scene_entities, model=load_model(model), texture=load_texture(texture), scale=scale, collider=collider, **kwargs)
        # les attributs avec des __ sont privés 
        self.__vitesseRotation = vitesse_rotation # attributs privés les __
        self.__speed = speed 
        self.master = master # le créateur de l'instance pour avoir des modifs sur celui ci
        #self.rotate(Vec3(0, 0, 0))

        #Rajouté pour la fonction de tours autour du soleil
        self.__rayon = self.position.x
        self.__stopped = False # si la simulation est stoppée pour observer les planètes
    
    @property
    def stopped(self):
        """
        POO avec la variable stopped pour pouvoir y acceder facilement
        avec un 
        self.stopped
        """
        return self.__stopped

    @stopped.setter
    def stopped(self, onoff: bool):
        """
        POO avec la variable stopped pour pouvoir la modifier facilement
        avec un 
        self.stopped = onoff : bool
        """
        self.__stopped=onoff

    @property
    def rayon(self):
        """
        POO avec la variable rayon pour pouvoir y acceder facilement
        avec un 
        self.rayon au lieu de self.__rayon
        """
        return self.__rayon

    @property
    def speed(self):
        """
        POO avec la variable speed pour pouvoir y acceder facilement
        avec un 
        self.speed
        """
        return self.__speed
    
    @property
    def vitesseRotation(self):
        """
        POO avec la variable vitesseRotation pour pouvoir y acceder facilement
        avec un 
        self.vitesseRotation
        """
        return self.__vitesseRotation
    
    @speed.setter
    def speed(self, value):
        """
        POO avec la variable speed pour pouvoir la modifier facilement
        avec un 
        self.speed = value : float
        """
        self.__speed = value
    
    @vitesseRotation.setter
    def vitesseRotation(self, value):
        """
        POO avec la variable vitesseRotation pour pouvoir la modifier facilement
        avec un 
        self.vitesseRotation = value : float
        """
        self.__vitesseRotation = value

    def my_update(self):
        """
        Fonction permettant de mettre à jour la planète dans l'espace 
        """
        #on update la position de la planète
        if self.stopped == False:
            self.rotation_y -= 50 * time.dt *self.speed # dt is short for delta time, the duration since the last frame.

            angle = time.time() * 50 *self.vitesseRotation # 50 degrés par seconde
    
            x = self.rayon * cos(radians(angle))
            z = self.rayon * sin(radians(angle))

            # On applique la nouvelle position
            self.position = (x, self.position.y, z)
    
    def on_click(self):
        """
        Méthode permmettant de repositionner la planète par rapport au point de vue de l'utilisateur"""
        print(f"Tu as clické sur {self.__class__.__name__}")
        camera.world_position = (self.position.x, self.position.y, self.position.z)
        self.master.world_position = camera.world_position

#Planet instanciation

class Saturne(Planet):
    def __init__(self,  model, texture, scale, collider, vitesse_rotation: int, speed: int, add_to_scene_entities=True, master=None,**kwargs):
        scale = scale * 9.14 # nombre de terres
        super().__init__(model, texture, scale, collider, vitesse_rotation, speed, add_to_scene_entities, **kwargs)
        self.__speed = speed # pour une vitesse de 1 normale # 34 848 km/h -> soleil
        self.__vitesseRotation = vitesse_rotation # 34 821 km/s
        #self.ellipse_rayon = 1 426 700 000 km
        #self.rayon = 58 232 km
        self.master = master

class Mars(Planet):
    def __init__(self, model, texture, scale, collider, vitesse_rotation: int, speed: int, add_to_scene_entities=True, master=None,**kwargs):
        scale = scale * 0.53
        super().__init__(model, texture, scale, collider, vitesse_rotation, speed, add_to_scene_entities, **kwargs)
        self.__vitesseRotation = self.vitesseRotation #868.220km/h
        self.__speed = speed # 86868km/h -> soleil
        #self.ellipse_rayon = 227 944 000 km
        #self.rayon = 3 390 km
        self.master = master

"""    def dessinerTrajectoire(self):
        # Calculer la distance entre l'entité cible et l'entité rayon
        distance = self.position
        radius = distance.length()

        # Créer une ellipse centrée sur l'entité cible et avec le rayon défini
        #self.ellipse = Ellipse(position=Vec3(0, 0, 0), radius=(radius, radius/2))
        ellipse = Ellipse(position=Vec3(0,0,0), radius=(radius, radius/2))
        ellipse.position=(Vec3(0,0,0))

        if self.updates%10:
            self.dessinerTrajectoire()
            self.updates = 0
        self.updates = self.updates +1"""

class Terre(Planet):
    def __init__(self,  model, texture, scale, collider, vitesse_rotation: int, speed: int, add_to_scene_entities=True,master=None, **kwargs):
        super().__init__(model, texture, scale, collider, vitesse_rotation, speed, add_to_scene_entities, **kwargs)
        self.__vitesseRotation = vitesse_rotation # 1 674,364 km/h
        self.__speed = speed # 107 320 km/h -> soleil
        #self.ellipse_rayon = 149 597 887,5 km
        #self.rayon = 6 371 km
        self.master = master

class Mercure(Planet):
    def __init__(self, model, texture, scale, collider, vitesse_rotation: int, speed: int, add_to_scene_entities=True, master=None,**kwargs):
        scale = scale *  0.38
        super().__init__(model, texture, scale, collider, vitesse_rotation, speed, add_to_scene_entities, **kwargs)
        self.__vitesseRotation = vitesse_rotation  #10,892 km/h
        self.__speed = speed # 172 332 km/h -> soleil
        #self.ellipse_rayon = 57 909 050 km
        #self.rayon = 2 440 km
        self.master = master

class Venus(Planet):
    def __init__(self,  model, texture, scale, collider, vitesse_rotation: int, speed: int, add_to_scene_entities=True, master=None,**kwargs):
        scale = scale * 0.95
        super().__init__(model, texture, scale, collider, vitesse_rotation, speed, add_to_scene_entities, **kwargs)
        self.__vitesseRotation = vitesse_rotation # 6,52 km/h
        self.__speed = speed # 126 072 km/h -> soleil
        #self.ellipse_rayon = 108 209 500 km
        #self.rayon = 6 052 km
        self.master = master

    def my_update(self):
        
        #on update la position de la planète
        if self.stopped == False:
            self.rotation_y -= 50 * time.dt *self.speed # dt is short for delta time, the duration since the last frame.
            angle = time.time() * 50 *self.vitesseRotation # 50 degrés par seconde
    
            x = self.rayon * cos(radians(angle))
            z = self.rayon * sin(radians(angle))

            # On applique la nouvelle position
            self.position = (x, self.position.y, z)


class Jupiter(Planet):
    def __init__(self, model, texture, scale, collider, vitesse_rotation: int, speed: int, add_to_scene_entities=True, master=None,**kwargs):
        scale = scale * 11
        super().__init__(model, texture, scale, collider, vitesse_rotation, speed, add_to_scene_entities, **kwargs)
        self.__vitesseRotation = vitesse_rotation # 47 051  km/h
        self.__speed = speed # 47 052 km/h -> soleil
        #self.ellipse_rayon = 778 340 000 km
        #self.rayon = 69 911 km
        self.master = master

class Uranus(Planet):
    def __init__(self, model, texture, scale, collider, vitesse_rotation: int, speed: int, add_to_scene_entities=True,master=None, **kwargs):
        scale = scale * 3.99
        super().__init__(model, texture, scale, collider, vitesse_rotation, speed, add_to_scene_entities, **kwargs)
        self.__vitesseRotation = vitesse_rotation # 9 320 km/h
        self.__speed = speed # 24 516 km/h -> soleil
        #self.ellipse_rayon = 2 870 700 000 km
        #self.rayon = 25 362 km
        self.master = master

class Neptune(Planet):
    def __init__(self, model, texture, scale, collider, vitesse_rotation: int, speed: int, add_to_scene_entities=True, master=None, **kwargs):
        scale = scale * 3.87
        super().__init__(model, texture, scale, collider, vitesse_rotation, speed, add_to_scene_entities, **kwargs)
        self.__vitesseRotation = vitesse_rotation # 9 660 km/h
        self.__speed = speed # 19 548 km/h -> soleil
        #self.ellipse_rayon = 4 498 400 000 km
        #self.rayon = 24 622 km
        self.master = master