#!/usr/bin/env python
import numpy as np
#
# This example creates a polygonal model of a sphere, and then renders it to
# the screen. It will rotate the sphere 360 degrees and then exit. The basic
# setup of source -> mapper -> actor -> renderer -> renderwindow is
# typical of most VTK programs.
#

#
# First we include the VTK Python packages that will make available
# all of the VTK commands to Python.
#
import vtk
import time
import sys
# Description de la scene
L = 10.
P = 5.
H = 4.

# Next we create an instance of vtkConeSource and set some of its
# properties. The instance of vtkConeSource "sphere" is part of a visualization
# pipeline (it is a source process object); it produces data (output type is
# vtkPolyData) which other filters may process.
#
sphere = vtk.vtkSphereSource()
sphere.SetPhiResolution( 20 )
sphere.SetThetaResolution( 20 )


#Cube pour le pourtour
cube = vtk.vtkCubeSource()
cube.SetXLength(L)
cube.SetYLength(H)
cube.SetZLength(P)

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


# In this example we terminate the pipeline with a mapper process object.
# (Intermediate filters such as vtkShrinkPolyData could be inserted in
# between the source and the mapper.)  We create an instance of
# vtkPolyDataMapper to map the polygonal data into graphics primitives. We
# connect the output of the sphere souece to the input of this mapper.
#
sphereMapper = vtk.vtkPolyDataMapper()
sphereMapper.SetLookupTable(tv)
sphereMapper.SetInputConnection( color_filter.GetOutputPort() )


#
# Create an actor to represent the sphere. The actor orchestrates rendering of
# the mapper's graphics primitives. An actor also refers to properties via a
# vtkProperty instance, and includes an internal transformation matrix. We
# set this actor's mapper to be sphereMapper which we created above.
#
sphereActor = vtk.vtkActor()
sphereActor.SetMapper( sphereMapper )
sphereActor.SetPosition(0., H, 0.)


cubeMapper = vtk.vtkPolyDataMapper()
cubeMapper.SetInputConnection(cube.GetOutputPort())


cubeActor = vtk.vtkActor()
cubeActor.SetMapper(cubeMapper)
cubeActor.GetProperty().SetRepresentationToWireframe()
cubeActor.SetPosition(L/2.,H/2.,P/2)


#
# Create the Renderer and assign actors to it. A renderer is like a
# viewport. It is part or all of a window on the screen and it is
# responsible for drawing the actors it has.  We also set the background
# color here
#
ren1= vtk.vtkRenderer()
ren1.AddActor( sphereActor )
ren1.AddActor( cubeActor )
ren1.SetBackground( 0.1, 0.2, 0.8 )
ren1.SetViewport(-L/2,-H/2,1.5*L,1.5*H)
#
# Finally we create the render window which will show up on the screen
# We put our renderer into the render window using AddRenderer. We also
# set the size to be 300 pixels by 300
#
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer( ren1 )
renWin.SetSize( 1000, 800 )

style = vtk.vtkInteractorStyleTrackball()

#renWin.Render()
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.SetInteractorStyle(style)
iren.Initialize()
iren.Start()

N=100
dx = L*1./(3.*N)
dy = -H*1./N
dz = -1./N
y = H
x = 0.
z = 0.
t = 0
dt = 1/100.
frein = 0.8
while True:
    time.sleep(0.01)
    t += dt
    x += t * dx
    y += t * dy
    z += t * dz
    if y < 0: 
        dy *= -frein 
        y = 0
    if y > H:
        dy *= -frein
        y = H
    if x < 0:
        dx *= -frein
        x = 0
    if x > L: 
        dx *= -frein
        x = L
    if z < 0:
        dz *= -frein
        z = 0
    if z > P: 
        dz *= -frein
        z = P
    sphereActor.SetPosition(x,y,z)
    renWin.Render()
    ren1.GetActiveCamera().Azimuth( 0.2 )
