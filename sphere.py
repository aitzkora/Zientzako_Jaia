from cree_scene import *
vx = 8.
vy = 3
vz = -5
y = H
x = L/2.
z = P/2. 
t = 0
dt = 1/100.
frein = 1. 

def animation(objet, evenement):
    global t,x,y,z,vx,vy,vz,dt
    t += dt
    x += dt * vx
    y += dt * vy
    z += dt * vz
    if y < 0: 
        vy *= -frein 
        y = 0
    if y > H:
        vy *= -frein
        y = H
    if x < 0:
        vx *= -frein
        x = 0
    if x > L: 
        vx *= -frein
        x = L
    if z < 0:
        vz *= -frein
        z = 0
    if z > P: 
        vz *= -frein
        z = P
    sphereActor.SetPosition(x,y,z)
    renWin.Render()
    #ren1.GetActiveCamera().Azimuth( 0.2 )

# initialization
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
#iren.SetInteractorStyle(style)
iren.Initialize()
iren.AddObserver('TimerEvent', animation)
iren.AddObserver('KeyPressEvent', PresseBouton)
timerId = iren.CreateRepeatingTimer(1);
iren.Start()
