import pgzrun

WIDTH=500
HEIGHT=500
TITLE="SpACE_Shooterz"
alien=Actor("alien")
message=""
def draw():
    screen.clear()
    screen.fill(color=(146,81,81))
    alien.draw()
    screen.draw.text(message, center=(400,0), fontsize=30)
def on_mouse_click(pos):
    global message
    if alien.colidepoint(pos):
        message="Good Shot!"

pgzrun.go()