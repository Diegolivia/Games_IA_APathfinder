from GameEngine import *

#Ajustar tamaño de la ventana
window=pyglet.window.Window(width=SIZE, height=SIZE)
fps_display=pyglet.window.FPSDisplay(window=window)

Game=Engine(imgPath)

def update(dt):
    pass

pyglet.clock.schedule_interval(update,1/60)

@window.event
def on_draw():
    window.clear()
    Gfx_batch.draw()
    fps_display.draw()

@window.event
def on_key_press(symbol,modifiers):
    if symbol == pyglet.window.key.R:
        Game.key_command(3)
    if symbol == pyglet.window.key.W:
        Game.key_command(4)


pyglet.app.run()