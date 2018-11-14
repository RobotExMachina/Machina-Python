"""
A convinient class of objects to communicate with Machina Bridge
by Ardavan Bidgoli
WIP
"""
import websockets
import asyncio

class MachinaRobot (object):

    def __init__(self, address = "ws://127.0.0.1:6999/Bridge", debug = False):
        # init 
        self.commands = []
        self.address = address
        self.debug = debug

        # error messages
        self.floatError = " must be a float."
        self.stringError = " must be a string."
        self.lsitError = " must be a list of strings."

    async def sendToBridge(self,address= "", command=""):
        # generic fucntion to communicate with web
        print (command)
        print (type(command))
        if not isinstance(command, str) :
            raise ValueError("command must be an string object.")
            
        if not isinstance(address, str) :
            raise ValueError("address must be an string object i.e.: \"ws://127.0.0.1:6999/Bridge\"")

        if address == "": 
            address = self.address

        print("sending to bridge...")

        async with websockets.connect(address) as websocket:
            # it waits until the ws sends the message
            await websocket.send(command)
            print("Message sent:{}".format(command))
            # then waits Bridge sends the feedback
            feedback = await websocket.recv()
            # then it prints the feedback
            print("Message Recieved:{}".format(feedback))


    def runCommands(self,cmds = ""):
        if cmds == "":
            cmds = self.commands

        if not isinstance(cmds, list) : 
            if isinstance(cmds, str) :
                cmds = [cmds]
            else:
                raise ValueError("command {}".format(self.listError))

        for cmd in cmds:
             
            if not isinstance(cmd, str) :
                raise ValueError("each command {}".format(self.stringError))
            #asyncio.get_event_loop().run_until_complete(self.sendToBridge(self.address,cmd))
            try:
                asyncio.get_event_loop().run_until_complete(self.sendToBridge(self.address,cmd))
            except:
                print ("FAIL: {}".format(cmd))
        return 


    def move(self, xInc, yInc, zInc = 0):
        if self.debug:
            if not isinstance(xInc, float):
                raise ValueError("xInc {}".format(floatError))
            if not isinstance(yInc, float):
                raise ValueError("yInc {}".format(floatError))
            if not isinstance(zInc, float):
                raise ValueError("zInc {}".format(floatError))

        self.commands = "Move({},{},{});".format(xInc, yInc, zInc) 
        self.runCommands()


    def moveTo (self,x,y,z):
        self.commands = "MoveTo({},{},{});".format(x, y, z) 
        self.runCommands()


    def transformTo(self,x,y,z,x0,x1,x2,y0,y1,y2):
        self.commands = "TransformTo({},{},{},{},{},{},{},{},{});".format(x,y,z,x0,x1,x2,y0,y1,y2) 
        self.runCommands()

    def rotate(self,x,y,z,angleInc):
        self.commands = "Rotate({},{},{},{});".format(x,y,z,angleInc) 
        self.runCommands()

    def rotateTo(self,x0,x1,x2,y0,y1,y2):
        self.commands = "RotateTo({},{},{},{},{},{});".format(x0,x1,x2,y0,y1,y2) 
        self.runCommands()

    def axes (self,j1,j2,j3,j4,j5,j6):
        self.commands = "Axes({},{},{},{},{},{});".format(j1,j2,j3,j4,j5,j6) 
        self.runCommands()

    def axesTo (self,j1,j2,j3,j4,j5,j6):
        self.commands = "AxesTo({},{},{},{},{},{});".format(j1,j2,j3,j4,j5,j6) 
        self.runCommands()  

    def speed(self,speedInc):
        self.commands = "Speed({});".format(speedInc) 
        self.runCommands()  

    def speedTo(self,speedVal):
        self.commands = "SpeedTo({});".format(speedVal) 
        self.runCommands()  

    def acceleration(self,accelerationInc):
        self.commands = "Acceleration({});".format(accelerationInc) 
        self.runCommands()  

    def accelerationTo(self,accelerationVal):
        self.commands = "AccelerationTo({});".format(accelerationVal) 
        self.runCommands()    


    def rotationSpeed(self,rotationSpeedInc):
        self.commands = "RotationSpeed({});".format(rotationSpeedInc) 
        self.runCommands()  

    def rotationSpeedTo(self,rotationSpeedVal):
        self.commands = "RotationSpeedTo({});".format(rotationSpeedVal) 
        self.runCommands()  

    def jointSpeed(self,jointSpeedInc):
        self.commands = "JointSpeed({});".format(jointSpeedInc) 
        self.runCommands()  

    def jointSpeedTo(self,jointSpeedVal):
        self.commands = "JointSpeedTo({});".format(jointSpeedVal) 
        self.runCommands()  

    def jointAcceleration(self,jointAccelerationInc):
        self.commands = "JointAcceleration({});".format(jointAccelerationInc) 
        self.runCommands()  

    def jointAccelerationTo(self,jointAccelerationVal):
        self.commands = "JointAccelerationTo({});".format(jointAccelerationVal) 
        self.runCommands()  

    def precision(self,precisionInc):
        self.commands = "Precision({});".format(PrecisionInc) 
        self.runCommands()  

    def precisionTo(self,precisionVal):
        self.commands = "PrecisionTo({});".format(precisionVal) 
        self.runCommands()  

    def motionMode(self,mode):
        self.commands = "MotionMode(\"{}\");".format(mode) 
        self.runCommands()  

    def message(self,msg):
        self.commands = "Message(\"{}\");".format(msg) 
        self.runCommands()  

    def wait(self,millis):
        self.commands = "Wait({});".format(millis) 
        self.runCommands()  

    def pushSettings(self):
        self.commands = "PushSettings();" 
        self.runCommands()  

    def popSettings(self):
        self.commands = "PopSettings();" 
        self.runCommands()  

    def toolCreate(self,name, x, y, z, x0, x1, x2, y0, y1, y2, weight, cogX, cogY, cogZ):
        self.commands =   "Tool.create(\"{}\",{},{},{},{},{},{},{},{},{},{},{},{},{},);".format(name, 
                                                                                                x, y, z, 
                                                                                                x0, x1, x2, 
                                                                                                y0, y1, y2, 
                                                                                                weight, 
                                                                                                cogX, cogY, cogZ)
        self.runCommands()


    def attach(self,name):
        self.commands = "Attach(\"{}\");".format(name) 
        self.runCommands()  

    def detach(self):
        self.commands = "Detach()" 
        self.runCommands()  

    def writeDigital(self,pin,on):
        self.commands = "WriteDigital({},{});".format(pin,on) 
        self.runCommands()  

    def writeAnalog(self,pin,value):
        self.commands = "WriteAnalog({},{});".format(pin,value) 
        self.runCommands()  

    def externalAxis (self,axisNumber, rxternalAxisInc):
        self.commands = "ExternalAxis({},{});".format(axisNumber, rxternalAxisInc) 
        self.runCommands()  
    
    def externalAxisTo (self,axisNumber, rxternalAxisVal):
        self.commands = "ExternalAxisTo({},{});".format(axisNumber, rxternalAxisVal) 
        self.runCommands()  
