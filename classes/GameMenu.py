from ursina import *
from ursina.prefabs.radial_menu import RadialMenu


class GameMenu(WindowPanel):
    def __init__(self, planets, **kwargs):
        self.button_group = ButtonGroup(('On', 'Off'), default="Off")
        self.button_group.on_value_changed = self.value_changed

        self.vitesseSlider = Slider(min=1, max=20)

        self.speedSlider = Slider(min=1, max=20)
        self.vitesseSlider.on_value_changed = self.slider_change
        self.speedSlider.on_value_changed = self.slider_change

        self.fovSlider = Slider(min = 50, max=160, default = 120, step = 1)
        self.fovSlider.on_value_changed = self.fov_changer

        self.buttonReset = Button(text="Paramètres initiaux")
        self.buttonReset.on_click = self.on_reset_click

        self.planets = planets # les différentes planètes instanciées

        self.planetsLastVitesseRotation = [] #on prends les dernières vitesse de Rotation et la vitesse pour garder une vitesse correcte
        self.planetsLastSpeed = []
        self.getBasicsPlanets() # on récupère toutes les qualifications des différentes planètes

        self.value : str 

        self.menu_enabled = False # valeur de si le menu est activé ou non
        self.changeMenu() #on desactive le menu pour pas qu'il soit affiché lors du lancement du jeu

        super().__init__(title="Menu Settings", content = (
            Text("Freeze Status : "),
            self.button_group,
            Text(text="Vitesse sur elle même : "),
            self.speedSlider,
            Text(text = "Vitesse de Rotation -> Soleil : "),
            self.vitesseSlider,
            Text(text="FOV : "),
            self.fovSlider,
            self.buttonReset,
            Button(text='Quitter le Menu', color=color.azure, on_click = self.changeMenu),
        ), **kwargs)
        self.y = self.panel.scale_y / 2 * self.scale_y

    def getBasicsPlanets(self):
        """
        On récupère les données initiales, telles que la vitesse sur elle meme, autour du soleil
        """
        for x in self.planets:
            self.planetsLastVitesseRotation.append(x.vitesseRotation)
            self.planetsLastSpeed.append(x.speed)

    def stopping_system(self):
        """
        Stopper le systeme solaire / le freeze
        """
        if self.value == "On":
            for planet in self.planets:
                planet.stopped = True
                
        elif self.value == "Off":
            for planet in self.planets:
                planet.stopped = False


    def changeMenu(self):
        """
        Changer le Status du menu, en l'occurrence :
         -> Affiché 
         -> Pas Affiché
         """
        if self.menu_enabled == False:
            self.enable()
            self.menu_enabled = True
        elif self.menu_enabled == True:
            self.disable()
            self.menu_enabled = False

    def slider_change(self):
        """
        Permet de changer chacune des valeurs pour chacun Slider modifié
        """
        speedModifier = self.speedSlider.value
        vitesseModifier = self.vitesseSlider.value

        for index, planet in enumerate(self.planets):
            planet.speed =  self.planetsLastSpeed[index] * speedModifier
            planet.vitesseRotation = self.planetsLastVitesseRotation[index] * vitesseModifier

    def fov_changer(self):
        """
        Permet de changer le fov s'il le slider est modifié
        """
        fove = self.fovSlider.value
        camera.fov = fove

    def value_changed(self):
        """
        Permet de voir si la valeur des boutons On/off a changé pour pouvoir activer ou désactiver le sys solaire
        """
        self.value = self.button_group.value
        self.stopping_system()

    def on_reset_click(self):
        """
        Si le bouton reset les paramètres est cliqué
        la fonction réinisialise les paramètres
        """
        self.button_group.value = "Off"
        self.value = "Off"
        self.vitesseSlider.value = 1
        self.fovSlider.value = 120
        self.speedSlider.value = 1
        self.value_changed()
        self.fov_changer()
        self.slider_change()
