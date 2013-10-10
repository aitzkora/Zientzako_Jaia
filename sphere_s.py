from cree_scene import *
vx = 8 
vy = -3
y = H
x = L/2.
z = P/2. 
t = 0
dt = 1/100.

def animation(objet, evenement):
    global t,x,y,z,vx,vy,dt
    t += dt
    x += dt * vx
    y += dt * vy
    if y < 0: 
        vy = -vy 
        y = 0
    if y > H:
        vy = -vy
        y = H
    if x < 0:
        vx = -vx 
        x = 0
    if x > L: 
        vx = -vx 
        x = L
    sphereActor.SetPosition(x,y,P/2)
    renWin.Render()

# initialization
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.Initialize()
iren.AddObserver('TimerEvent', animation)
iren.AddObserver('KeyPressEvent', PresseBouton)
timerId = iren.CreateRepeatingTimer(1);
iren.Start()
