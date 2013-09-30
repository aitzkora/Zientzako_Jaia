from cree_scene import *
import time

x = L/2. 
y = H
z = P/2.
dt = 1/100.
vy = -3

for t in range(100):
    time.sleep(0.01)
    t += dt
    y += dt * vy
    sphereActor.SetPosition(x,y,z)
    renWin.Render()
    #ren1.GetActiveCamera().Azimuth( 0.2 )
