from cree_scene import *
vy = 3
y = H
x = L/2.
z = P/2. 
t = 0
dt = 1/100.
frein = 1. 

######################
# FONCTION d'animation
#######################

def animation(objet, evenement):
    global t,x,y,z,vy,dt
    t += dt
    y += dt * vy
    sphereActor.SetPosition(x,y,z)
    renWin.Render()
    #ren1.GetActiveCamera().Azimuth( 0.2 )

# 
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.Initialize()

iren.AddObserver('TimerEvent', animation)
timerId = iren.CreateRepeatingTimer(1);
iren.Start()
