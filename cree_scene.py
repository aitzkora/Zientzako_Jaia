import vtk
# Description de la scene
L = 10.
P = 5.
H = 4.

##################
# SPHERE
##################

# On cree une source (en l'occurence une sphere pour le pipeline vtk)
sphere = vtk.vtkSphereSource()
sphere.SetPhiResolution( 20 )
sphere.SetThetaResolution( 20 )

#Filtre de coloration
color_filter = vtk.vtkElevationFilter();
color_filter.SetInputConnection(sphere.GetOutputPort())
color_filter.SetLowPoint(0,0,-0.5);
color_filter.SetHighPoint(0,0,0.5);

# table de valeurs 
tv = vtk.vtkLookupTable()
tv.SetHueRange(0.667,0.)
tv.SetSaturationRange(1,1)
tv.SetValueRange(1,1)

# on utiliseur un traceur avec qui colore la sphere selon sa hauteur suivant l'axe
# des z a l'aide d'un filtre de coloration
sphereMapper = vtk.vtkPolyDataMapper()
sphereMapper.SetLookupTable(tv)
sphereMapper.SetInputConnection( color_filter.GetOutputPort() )

# Acteur associe a la sphere : il prend un traceur en entree
# c'est cet acteur qu'on va modifier au cours de l'animation
sphereActor = vtk.vtkActor()
sphereActor.SetMapper( sphereMapper )
sphereActor.SetPosition(L/2., H, P/2)

#########
# CUBE 
#########
# on cree une autre source (un cube) pour donner un cadre ou rebondir
cube = vtk.vtkCubeSource()
cube.SetXLength(L)
cube.SetYLength(H)
cube.SetZLength(P)

# traceur du cube (on le connecte en sortie de la source cube)
cubeMapper = vtk.vtkPolyDataMapper()
cubeMapper.SetInputConnection(cube.GetOutputPort())

# on cree un acteur pour le cube. 
# comme on veut voir au travers on le dessine en file de fer
cubeActor = vtk.vtkActor()
cubeActor.SetMapper(cubeMapper)
cubeActor.GetProperty().SetRepresentationToWireframe()
cubeActor.SetPosition(L/2.,H/2.,P/2)

#########
# RENDU
#########
# On cree un moteur de rendu (renderer) auquel on ajoute
# comme acteurs la sphere et le cube
# on regle differents parametres
ren1= vtk.vtkRenderer()
ren1.AddActor( sphereActor )
ren1.AddActor( cubeActor )
ren1.SetBackground( 0.1, 0.2, 0.8 )
ren1.SetViewport(-L/2,-H/2,1.5*L,1.5*H)

##################
# FENETRE DE RENDU
###################
# finalement on cree une fenetre de rendu 
# associe au moteur de rendu
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer( ren1 )
renWin.SetSize( 1000, 800 )
