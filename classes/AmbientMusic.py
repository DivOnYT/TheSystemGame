from ursina import *
from random import randrange

#Music Link from Youtube
# https://www.youtube.com/watch?v=teEPbg4u7xQ

class AmbientMusic(Audio):
    """
    Classe Permettant de jouer un fichier audio en boucle en choisissant un moment aléatoire de celle ci pour se lancer permmettant
    de donner un nouveau son à chaque visite de la représentation en 3D"""
    def __init__(self, sound_file_name='Resources/music-space.mp3', autoplay=True, auto_destroy=False, loop= True,**kwargs):

        super().__init__(sound_file_name, autoplay, auto_destroy, loop=loop, **kwargs)

        self.volume_multiplier = 40  # le multiplier de volume par défaut pour la classe
        self.volume = 10 # le volume de base
        self.balance = 2 # et la balance des sons par défaut
        
        self.__listening = True  # si l'utilisateur est actuellement en train d'écouter
        self.lastTime : float # dernier moment d'écoute si le morceau est coupé par la touche m

        self.randSong() # moment aléatoire

    def randSong(self):
        """
        Fonction permettant de lancer la musique à un moment aléatoire et est utilisée à l'initialisation de la classe"""
        self.stop()
        time = randrange(0, int(self.length))
        self.play(start=time)
        print(f"[AmbientMusic] - Le Morceau a été lancé à {time} secondes du début.")

    @property
    def listening(self):
        return self.__listening

    @listening.setter
    def listening(self, value : bool):
        if value == self.__listening:
            return
        
        valeur = ""
        
        self.__listening = value
        if value == True:

            self.play(self.lastTime)
            valeur = "lancé"

        elif value == False:

            self.stop()
            self.lastTime = self.time
            valeur = "arrêté"

        print(f"[AmbientMusic] - Le Morceau a été {valeur}.")