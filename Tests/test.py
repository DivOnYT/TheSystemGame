from ursina import Ursina, Sky, load_model, color, Text, window
from ursina import *
app = Ursina(vsync=False)
'''
Simple camera for debugging.
Hold right click and move the mouse to rotate around point.
'''

sky = Sky()
e = Entity(model=load_model('cube', use_deepcopy=True), color=color.white, collider='box')
e.model.colorize()

from ursina.prefabs.first_person_controller import FirstPersonController

ground = Entity(model='sphere', scale=32, texture='white_cube', texture_scale=(32,32), collider='box')
box = Entity(model='cube', collider='box', texture='white_cube', scale=(10,2,2), position=(2,1,5), color=color.light_gray)
player = FirstPersonController(y=1, enabled=True)

ec = EditorCamera()
ec.enabled = False
rotation_info = Text(position=window.top_right)

def update():
    rotation_info.text = str(int(ec.rotation_y)) + '\n' + str(int(ec.rotation_x))


def input(key):
    if key == 'tab':    # press tab to toggle edit/play mode
        ec.enabled = not ec.enabled
        player.enabled = not player.enabled

app.run()