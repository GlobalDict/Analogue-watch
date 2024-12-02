# GlobalDict :)

from Range import *
from math import *

class Analogue(types.KX_PythonComponent):
    args = {}
    
    def awake(self, args):

        self.mouse = logic.mouse

        self.sec = 0

        self.objects = self.object.scene.objects
        self.second = self.objects["SecondHandle"]
        self.minute = self.objects["MinuteHandle"]
        self.hour = self.objects["HourHandle"]

        self.selector = self.objects["Selector"]
        self.minP = self.objects["MinP"]
        self.minM = self.objects["MinM"]
        self.hrP = self.objects["HrP"]
        self.hrM = self.objects["HrM"]
        
    def start(self, args):
        pass

    def buttons(self):
        # Store mouse cursor's x and y position in a list
        cood = [self.mouse.position[0], self.mouse.position[1]]

        # Get screen ray casted from the camera to mouse cursor
        mouseOver = self.objects["Camera"].getScreenRay(cood[0], cood[1], 5)

        # Change selector object's color on hover and press
        def changeColor():
            if self.mouse.inputs[events.LEFTMOUSE].active:
                self.selector.meshes[0].materials[0].diffuseColor = (0.579007, 0.002586, 0)
            else:
                self.selector.meshes[0].materials[0].diffuseColor = (0.203893, 0.104274, 0.01195)

        # Minutes plus button
        if mouseOver == self.minP:
            self.selector.worldPosition = self.minP.worldPosition
            changeColor()

            if self.mouse.inputs[events.LEFTMOUSE].activated:
                for i in range(1):
                    self.minute.applyRotation([0, 0, -radians(6)])
        
        # Minutes minus button
        elif mouseOver == self.minM:
            changeColor()
            self.selector.worldPosition = self.minM.worldPosition

            if self.mouse.inputs[events.LEFTMOUSE].activated:
                for i in range(1):
                    self.minute.applyRotation([0, 0, radians(6)])

        # Hours plus button
        elif mouseOver == self.hrP:
            changeColor()
            self.selector.worldPosition = self.hrP.worldPosition

            if self.mouse.inputs[events.LEFTMOUSE].activated:
                for i in range(1):
                    self.hour.applyRotation([0, 0, -radians(6)])

        # Hours minus button
        elif mouseOver == self.hrM:
            changeColor()
            self.selector.worldPosition = self.hrM.worldPosition

            if self.mouse.inputs[events.LEFTMOUSE].activated:
                for i in range(1):
                    self.hour.applyRotation([0, 0, radians(6)])
        
        # Reset selector's position
        else:
            self.selector.worldPosition = (-3, 3, 0)

    def update(self):

        self.sec += 1*logic.deltaTime()
        self.buttons()

        if self.sec >= 1:
            for i in range(1):

                # Rotate the second hand clockwise
                self.second.applyRotation([0,0,radians(-6)])

                # Rotate the minute hand clockwise
                self.minute.applyRotation([0,0,-radians(0.1)])

                # Rotate the hour hand clockwise
                self.hour.applyRotation([0,0,-radians(0.0083333333333333)])
                
                # Reset self.sec 
                self.sec = 0
