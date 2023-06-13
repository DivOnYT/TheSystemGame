from ursina import *
from classes.Stars import Stars
from classes.Planets import *
from classes.Sun import Sun
from classes.GameMenu import GameMenu
from classes.AmbientMusic import AmbientMusic
from ursina import window
from classes.SplashScreen import SplashScreen
from ursina.prefabs.radial_menu import RadialMenu, RadialMenuButton
import __main__

window.title = "Système Solaire par Côme d'Hérouville et Adrien Rousseau"


class Application(Ursina):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Paramètres importants
        window.borderless = 0
        window.vsync = 1
        window.center_on_screen = True
        window.fullscreen = True
        self.tailleInit = 100 # Zoom x100
        self.basic_taille = self.tailleInit
        self.planets = []
        self.sun : Sun
        self.tailleTerre = - 1750
        scene.clear()
        #lancement du SplashScreen
        splash = SplashScreen(name='splash_systeme_solaire', parent=camera.ui, texture="Resources/logo.png", world_z=camera.overlay.z-1, scale=.1)
        self.reload()

    def change_taille(self, taille: float):
        """
        Permet de changer la taille du système solaire et de recharger le modèle"""
        self.basic_taille = self.basic_taille * taille
        self.reload()
    
    def input(self, key, is_raw=False):
        """Built-in input handler. Propagates the input to all entities and the input function of the main script. MAin use case for this it to simulate input though code, like: app.input('a').
        Args:
            key (Any): The input key.
            is_raw (bool, optional): Whether or not the input should be treated as "raw". Defaults to False.


        Fonction par défaut de la classe mère Ursina et copié collée pour  garder certains attributs intéréssants notamment les touches rentrées et 
        pouvoir modifier l'action effectuée
        """
        if key == "m": # permettant de couper la musique à tout moment
            if self.music.listening == True:
                self.music.listening = False
            elif self.music.listening == False:
                self.music.listening = True

        # NON MODIFIE
        keyboard_keys = '1234567890qwertyuiopasdfghjklzxcvbnm'
        if not is_raw and key in keyboard_keys:
            return

        if not 'mouse' in key:
            for prefix in ('control-', 'shift-', 'alt-'):
                if key.startswith(prefix):
                    key = key.replace('control-', '')
                    key = key.replace('shift-', '')
                    key = key.replace('alt-', '')
                    if key in keyboard_keys:
                        return

        if key in self._input_name_changes:
            key = self._input_name_changes[key]

        if key in input_handler.rebinds:
            key = input_handler.rebinds[key]

        input_handler.input(key)

        if not application.paused:
            if hasattr(__main__, 'input'):
                __main__.input(key)

        for entity in scene.entities:
            if entity.enabled == False or entity.ignore or entity.ignore_input:
                continue
            if application.paused and entity.ignore_paused == False:
                continue

            if hasattr(entity, 'input') and callable(entity.input):
                if entity.input(key):
                    break

            if hasattr(entity, 'scripts'):
                for script in entity.scripts:
                    if script.enabled and hasattr(script, 'input') and callable(script.input):
                        if script.input(key):
                            break


        mouse.input(key)

        # Modifié

        if held_keys["escape"]: #chargement du menu à la touche echap
            #Implementation du menu principal de controle
            self.menu.changeMenu()

    def createMenu(self):
        """
        Fonction permettant de créeer le menu
        """
        self.menu = GameMenu(planets=self.planets)
        self.menu.changeMenu()

    
    def reload(self):
        self.music = AmbientMusic(sound_file_name="Resources/music-space.mp3")

        #Creating all the solar system
        sun = Sun(self, scale=self.basic_taille+30)
        AmbientLight(parent=sun, y=0, z=0, shadows=True)

        mercure = Mercure(master=self, model='sphere', texture='Textures/Mercure.jpg', scale = self.basic_taille, collider='box', position = Vec3(self.tailleTerre*0.5, sun.scale.y/2, 0),vitesse_rotation=1, speed=1)
        self.planets.append(mercure)

        venus = Venus(master=self, model='sphere', texture='Textures/Venus.jpg', scale = self.basic_taille, collider='box', position = Vec3(self.tailleTerre*0.7233, sun.scale.y/2-50, 0),vitesse_rotation=1/2, speed=1)
        self.planets.append(venus)

        terre = Terre(master=self, model='Models/Earth.obj', texture='Textures/Earth.png', scale = self.basic_taille/2, collider='box', position = Vec3(self.tailleTerre, sun.scale.y/2, 0),vitesse_rotation=1/3, speed=1)
        self.planets.append(terre)

        mars = Mars(master=self, model='Models/Mars.obj', texture='Textures/Mars.png', scale = self.basic_taille/4, collider='box', position = Vec3(self.tailleTerre*1.5237, sun.scale.y/2, 0),vitesse_rotation=1/4, speed=1)
        self.planets.append(mars)

        jupiter = Jupiter(master=self, model='sphere', texture='Textures/jupiter.jpg', scale = self.basic_taille, collider='box', position = Vec3(self.tailleTerre*2.1067, sun.scale.y/2-500, 0),vitesse_rotation=1/5, speed=1)
        self.planets.append(jupiter)

        saturne = Saturne(master=self, model='sphere', texture='Textures/saturn.jpg', scale = self.basic_taille/1.4, collider='box', position = Vec3(self.tailleTerre*3.087, sun.scale.y/2-300, 0),vitesse_rotation=1/6, speed=1)
        self.planets.append(saturne)

        uranus = Uranus(master=self, model='sphere', texture='Textures/uranus.jpg', scale = self.basic_taille, collider='box', position = Vec3(self.tailleTerre*4, sun.scale.y/2-500, 0),vitesse_rotation=1/7, speed=1)
        self.planets.append(uranus)

        neptune = Neptune(master=self, model='sphere', texture='Textures/neptune.jpg', scale = self.basic_taille/2, collider='box', position = Vec3(self.tailleTerre*4.4, sun.scale.y/2, 0),vitesse_rotation=1/8, speed=1)
        self.planets.append(neptune)
        
        #Instanciation du Menu
        self.createMenu()
        
        
        #Create the Buttons
        #b = Button(text="Stop All", radius=0.3,scale=.25, text_origin=(-.5,0), on_click = self.stopping_system)
        """wp = WindowPanel(
            title='Settings',
            content=(
            Text('Name:'),
            InputField(name='name_field'),
            Button(text='Submit', color=color.azure),
            Slider(),
            Slider(),
            ButtonGroup(('test', 'eslk', 'skffk'))
            ),
        )
        wp.y = wp.panel.scale_y / 2 * wp.scale_y
        """
        # Setting the stars background
        Stars()

        # Setting up the camera settings
        camera.position = (500, sun.scale.y/2, -8000)
        camera.look_at(sun)
        camera.fov = 120 #120

        #Settings the differents updates to do with the differents planets
        mercure.update = mercure.my_update
        venus.update = venus.my_update
        terre.update = terre.my_update
        mars.update = mars.my_update
        jupiter.update = jupiter.my_update
        saturne.update = saturne.my_update
        uranus.update = uranus.my_update
        neptune.update = neptune.my_update

        #Mettre la camera en mode editeur pour se déplacer et avoir une meilleure vue des différentes planètes
        self.ec = EditorCamera()



if __name__ == "__main__": # Testing the application
    app = Application() #Instanciate the main class to do the app

    # APP settings
    app.development_mode = False

    #Running the app
    app.run()