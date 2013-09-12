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

#
# Next we create an instance of vtkConeSource and set some of its
# properties. The instance of vtkConeSource "sphere" is part of a visualization
# pipeline (it is a source process object); it produces data (output type is
# vtkPolyData) which other filters may process.
#
sphere = vtk.vtkSphereSource()
sphere.SetRadius( 1. )
sphere.SetPhiResolution( 30 )
sphere.SetThetaResolution( 30 )

#
# In this example we terminate the pipeline with a mapper process object.
# (Intermediate filters such as vtkShrinkPolyData could be inserted in
# between the source and the mapper.)  We create an instance of
# vtkPolyDataMapper to map the polygonal data into graphics primitives. We
# connect the output of the sphere souece to the input of this mapper.
#
sphereMapper = vtk.vtkPolyDataMapper()
sphereMapper.SetInputConnection( sphere.GetOutputPort() )

# Description de la scene
L = 10.
P = 1.
H = 4

#
# Create an actor to represent the sphere. The actor orchestrates rendering of
# the mapper's graphics primitives. An actor also refers to properties via a
# vtkProperty instance, and includes an internal transformation matrix. We
# set this actor's mapper to be sphereMapper which we created above.
#
sphereActor = vtk.vtkActor()
sphereActor.SetMapper( sphereMapper )
sphereActor.SetPosition(0., H, 0.)
#
# Create the Renderer and assign actors to it. A renderer is like a
# viewport. It is part or all of a window on the screen and it is
# responsible for drawing the actors it has.  We also set the background
# color here
#
ren1= vtk.vtkRenderer()
ren1.AddActor( sphereActor )
ren1.SetBackground( 0.1, 0.2, 0.8 )
ren1.SetViewport(-L/2,-H/2,1.5*L,1.5*H)
ren1.GetActiveCamera().SetPosition(0,0,1)
#
# Finally we create the render window which will show up on the screen
# We put our renderer into the render window using AddRenderer. We also
# set the size to be 300 pixels by 300
#
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer( ren1 )
renWin.SetSize( 1000, 800 )

max_it = 100


def f_pos(i):
    x = float(i)/max_it * L
    y = H - float(i)/max_it * H/2 
    return x,y


#
# now we loop over 360 degreeees and render the sphere each time
#
for i in range(max_it):
    time.sleep(0.01)
    x,y = f_pos(i)
    sphereActor.SetPosition(x,y,0.)
    renWin.Render()
    #ren1.GetActiveCamera().Azimuth( 1 )
