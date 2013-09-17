from cree_scene import *
import time


for i in range(100):
    time.sleep(0.01)
    sphereActor.SetPosition(0,H,P/2-i*5./100)
    renWin.Render()
    #ren1.GetActiveCamera().Azimuth( 0.2 )
