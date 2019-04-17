"""
A convinient class of objects to communicate with Machina Bridge
by Ardavan Bidgoli and Ozguc Bertug Capunaman
Robotics Fellows at CMU
WIP
"""
import websockets
import asyncio

class MachinaRobot (object):

    def __init__(self, address = "ws://127.0.0.1:6999/Bridge", debug = False):
        # init 
        self.command = ""
        self.commands = []
        self.address = address
        self.debug = debug

        # error messages
        self.floatError = " must be a float."
        self.stringError = " must be a string."
        self.listError = " must be a list of strings."
        self.intError = " must be an integer."
        self.externalAxisError = " must be between 1 and 6."


    async def sendToBridge(self,address= "", command=""):
        # generic function to communicate with web
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

    async def sendQueueToBridge(self,address= "", commands= ""):
        # generic function to communicate with web
        if not isinstance(command, str) :
            raise ValueError("command must be an string object.")
            
        if not isinstance(address, str) :
            raise ValueError("address must be an string object i.e.: \"ws://127.0.0.1:6999/Bridge\"")

        if address == "": 
            address = self.address
        if commands == "":
            commands = self.commands

        print("sending to bridge...")

        async with websockets.connect(address) as websocket:
            while len(commands) > 0:
                command = commands.pop(0)
                # it waits until the ws sends the message
                await websocket.send(command)
                print("Message sent:{}".format(command))
                # then waits Bridge sends the feedback
                feedback = await websocket.recv()
                # then it prints the feedback
                print("Message Recieved:{}".format(feedback))


    def runCommand(self,cmd = ""):
        if cmd == "":
            cmd = self.command

        if cmd == "":
            raise ValueError("command missing.")

        if not isinstance(cmd, str) :
            raise ValueError("each command {}".format(self.stringError))

        try:
            asyncio.get_event_loop().run_until_complete(self.sendToBridge(self.address,cmd))
        except:
            print ("FAIL: {}".format(cmd))
        self.command = ""
        return 

    def runQueuedCommands(self,cmds = ""):
        if cmds == "":
            cmds = self.commands

        if not isinstance(cmds, list) : 
            if isinstance(cmds, str) :
                cmds = [cmds]
            else:
                raise ValueError("command {}".format(self.listError))

        try:
            asyncio.new_event_loop().run_until_complete(self.sendQueueToBridge())
        except:
            print ("FAILED TO RUN STACKED COMMANDS")
        return

    ##  ███████╗███████╗████████╗████████╗██╗███╗   ██╗ ██████╗ ███████╗
    ##  ██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝ ██╔════╝
    ##  ███████╗█████╗     ██║      ██║   ██║██╔██╗ ██║██║  ███╗███████╗
    ##  ╚════██║██╔══╝     ██║      ██║   ██║██║╚██╗██║██║   ██║╚════██║
    ##  ███████║███████╗   ██║      ██║   ██║██║ ╚████║╚██████╔╝███████║
    ##  ╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝

    def speed(self,speedInc):
        self.command = "Speed({});".format(speedInc) 
        self.runCommand()
        return

    def queueSpeed(self,speedInc):
        self.commands.append("Speed({});".format(speedInc))
        return  

    def speedTo(self,speedVal):
        self.command = "SpeedTo({});".format(speedVal) 
        self.runCommand()
        return  

    def queueSpeedTo(self,speedVal):
        self.commands.append("SpeedTo({});".format(speedVal))
        return 

    def acceleration(self,accelerationInc):
        self.command = "Acceleration({});".format(accelerationInc) 
        self.runCommand()
        return  

    def queueAcceleration(self,accelerationInc):
        self.commands.append("Acceleration({});".format(accelerationInc))
        return

    def accelerationTo(self,accelerationVal):
        self.command = "AccelerationTo({});".format(accelerationVal) 
        self.runCommand()
        return

    def queueAccelerationTo(self,accelerationVal):
        self.commands.append("AccelerationTo({});".format(accelerationVal))
        return   

    def rotationSpeed(self,rotationSpeedInc):
        self.command = "RotationSpeed({});".format(rotationSpeedInc) 
        self.runCommand()
        return

    def queueRotationSpeed(self,rotationSpeedInc):
        self.commands.append("RotationSpeed({});".format(rotationSpeedInc))
        return 

    def rotationSpeedTo(self,rotationSpeedVal):
        self.command = "RotationSpeedTo({});".format(rotationSpeedVal) 
        self.runCommand()
        return 

    def queueRotationSpeedTo(self,rotationSpeedVal):
        self.commands.append("RotationSpeedTo({});".format(rotationSpeedVal))
        return 

    def jointSpeed(self,jointSpeedInc):
        self.command = "JointSpeed({});".format(jointSpeedInc) 
        self.runCommand()
        return  

    def queueJointSpeed(self,jointSpeedInc):
        self.commands.append("JointSpeed({});".format(jointSpeedInc))
        return  

    def jointSpeedTo(self,jointSpeedVal):
        self.command = "JointSpeedTo({});".format(jointSpeedVal) 
        self.runCommand()
        return

    def queueJointSpeedTo(self,jointSpeedVal):
        self.commands.append("JointSpeedTo({});".format(jointSpeedVal))
        return 

    def jointAcceleration(self,jointAccelerationInc):
        self.command = "JointAcceleration({});".format(jointAccelerationInc) 
        self.runCommand()
        return  

    def queueJointAcceleration(self,jointAccelerationInc):
        self.commands.append("JointAcceleration({});".format(jointAccelerationInc))
        return  

    def jointAccelerationTo(self,jointAccelerationVal):
        self.command = "JointAccelerationTo({});".format(jointAccelerationVal) 
        self.runCommand()
        return  

    def queueJointAccelerationTo(self,jointAccelerationVal):
        self.commands.append("JointAccelerationTo({});".format(jointAccelerationVal))
        return 

    def precision(self,precisionInc):
        self.command = "Precision({});".format(PrecisionInc) 
        self.runCommand()
        return

    def queuePrecision(self,precisionInc):
        self.commands.append("Precision({});".format(PrecisionInc))
        return 

    def precisionTo(self,precisionVal):
        self.command = "PrecisionTo({});".format(precisionVal) 
        self.runCommand()
        return

    def queuePrecisionTo(self,precisionVal):
        self.commands.append("PrecisionTo({});".format(precisionVal))
        return  

    def motionMode(self,mode):
        # motion type should be "linear" or "joint" as string
        if self.debug:
            if not isinstance(motionType, string):
                raise ValueError("motionType {}".format(stringError))  

        self.command = "MotionMode(\"{}\");".format(mode) 
        self.runCommand()
        return

    def queueMotionMode(self,mode):
        # motion type should be "linear" or "joint" as string
        if self.debug:
            if not isinstance(motionType, string):
                raise ValueError("motionType {}".format(stringError))  

        self.commands.append("MotionMode(\"{}\");".format(mode))
        return   


    ##   █████╗  ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗
    ##  ██╔══██╗██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
    ##  ███████║██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗
    ##  ██╔══██║██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║
    ##  ██║  ██║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║
    ##  ╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
        
    def move(self, xInc, yInc, zInc = 0):
        if self.debug:
            if not isinstance(xInc, float):
                raise ValueError("xInc {}".format(floatError))
            if not isinstance(yInc, float):
                raise ValueError("yInc {}".format(floatError))
            if not isinstance(zInc, float):
                raise ValueError("zInc {}".format(floatError))

        self.command = "Move({},{},{});".format(xInc, yInc, zInc) 
        self.runCommand()
        return

    def queueMove(self, xInc, yInc, zInc = 0):
        if self.debug:
            if not isinstance(xInc, float):
                raise ValueError("xInc {}".format(floatError))
            if not isinstance(yInc, float):
                raise ValueError("yInc {}".format(floatError))
            if not isinstance(zInc, float):
                raise ValueError("zInc {}".format(floatError))

        self.commands.append("Move({},{},{});".format(xInc, yInc, zInc))
        return
        
    def moveTo (self,x,y,z):
        if self.debug:
            if not isinstance(x, float):
                raise ValueError("x {}".format(floatError))
            if not isinstance(y, float):
                raise ValueError("y {}".format(floatError))
            if not isinstance(z, float):
                raise ValueError("z {}".format(floatError))
        self.command = "MoveTo({},{},{});".format(x, y, z) 
        self.runCommand()
        return

    def queueMoveTo (self,x,y,z):
        if self.debug:
            if not isinstance(x, float):
                raise ValueError("x {}".format(floatError))
            if not isinstance(y, float):
                raise ValueError("y {}".format(floatError))
            if not isinstance(z, float):
                raise ValueError("z {}".format(floatError))
        self.commands.append("MoveTo({},{},{});".format(x, y, z))
        return


    def externalAxis(self,axisNumber,increment):
        if self.debug:
            if not isinstance(axisNumber, int):
                raise ValueError("axisNumber {}".format(intError))

            if 1> axisNumber or axisNumber >6 :
                raise ValueError("axisNumber {}".format(externalAxisError))

            if not isinstance(increment, float):
                raise ValueError("increment {}".format(floatError))

        self.command = "ExternalAxis({},{});".format(axisNumber, increment) 
        self.runCommand()
        return

    def queueExternalAxis(self,axisNumber,increment):
        if self.debug:
            if not isinstance(axisNumber, int):
                raise ValueError("axisNumber {}".format(intError))

            if 1> axisNumber or axisNumber >6 :
                raise ValueError("axisNumber {}".format(externalAxisError))

            if not isinstance(increment, float):
                raise ValueError("increment {}".format(floatError))

        self.commands.append("ExternalAxis({},{});".format(axisNumber, increment))
        return

    def externalAxisTo(self,axisNumber, val):
        if self.debug:
            if not isinstance(axisNumber, int):
                raise ValueError("axisNumber {}".format(intError))

            if 1> axisNumber or axisNumber >6 :
                raise ValueError("axisNumber {}".format(externalAxisError))

            if not isinstance(val, float):
                raise ValueError("val {}".format(floatError))

        self.command = "ExternalAxisTo({},{});".format(axisNumber, val) 
        self.runCommand()
        return

 def queueExternalAxisTo(self,axisNumber, val):
        if self.debug:
            if not isinstance(axisNumber, int):
                raise ValueError("axisNumber {}".format(intError))

            if 1> axisNumber or axisNumber >6 :
                raise ValueError("axisNumber {}".format(externalAxisError))

            if not isinstance(val, float):
                raise ValueError("val {}".format(floatError))

        self.commands.append("ExternalAxisTo({},{});".format(axisNumber, val))
        return

    def transformTo(self,x,y,z,x0,x1,x2,y0,y1,y2):
        self.command = "TransformTo({},{},{},{},{},{},{},{},{});".format(x,y,z,x0,x1,x2,y0,y1,y2) 
        self.runCommand()
        return

    def queueTransformTo(self,x,y,z,x0,x1,x2,y0,y1,y2):
        self.commands.append("TransformTo({},{},{},{},{},{},{},{},{});".format(x,y,z,x0,x1,x2,y0,y1,y2))
        return

    def rotate(self,x,y,z,angleInc):
        self.command = "Rotate({},{},{},{});".format(x,y,z,angleInc) 
        self.runCommand()
        return

    def queueRotate(self,x,y,z,angleInc):
        self.commands.append("Rotate({},{},{},{});".format(x,y,z,angleInc))
        return

    def rotateTo(self,x0,x1,x2,y0,y1,y2):
        self.command = "RotateTo({},{},{},{},{},{});".format(x0,x1,x2,y0,y1,y2) 
        self.runCommand()
        return

    def queueRotateTo(self,x0,x1,x2,y0,y1,y2):
        self.commands.append("RotateTo({},{},{},{},{},{});".format(x0,x1,x2,y0,y1,y2))
        return

    def axes (self,j1,j2,j3,j4,j5,j6):
        self.command = "Axes({},{},{},{},{},{});".format(j1,j2,j3,j4,j5,j6) 
        self.runCommand()
        return

    def queueAxes (self,j1,j2,j3,j4,j5,j6):
        self.commands.append("Axes({},{},{},{},{},{});".format(j1,j2,j3,j4,j5,j6))
        return

    def axesTo (self,j1,j2,j3,j4,j5,j6):
        self.command = "AxesTo({},{},{},{},{},{});".format(j1,j2,j3,j4,j5,j6) 
        self.runCommand()
        return

    def queueAxesTo (self,j1,j2,j3,j4,j5,j6):
        self.commands.append("AxesTo({},{},{},{},{},{});".format(j1,j2,j3,j4,j5,j6))
        return

    def queueAxesTo (self,j1,j2,j3,j4,j5,j6):
        self.commands.append("AxesTo({},{},{},{},{},{});".format(j1,j2,j3,j4,j5,j6))
        return 

    def message(self,msg):
        self.command = "Message(\"{}\");".format(msg) 
        self.runCommand()
        return

    def queueMessage(self,msg):
        self.commands.append("Message(\"{}\");".format(msg))
        return

    def wait(self,millis):
        self.command = "Wait({});".format(millis) 
        self.runCommand()
        return

    def queueWait(self,millis):
        self.commands.append("Wait({});".format(millis))
        return  

    def pushSettings(self):
        self.command = "PushSettings();" 
        self.runCommand()
        return  

    def queuePushSettings(self):
        self.commands.append("PushSettings();")
        return 

    def popSettings(self):
        self.command = "PopSettings();" 
        self.runCommand()
        return

    def queuePopSettings(self):
        self.commands.append("PopSettings();")
        return

###
    def defineTool(self,name, x, y, z, VXx, VXy, Vxz, VYx, VYy, VYz, weight, cogX, cogY, cogZ):
        self.command =   "DefineTool(\"{}\",{},{},{},{},{},{},{},{},{},{},{},{},{});".format(name,
                                                                                                x, y, z,
                                                                                                VXx, VXy, Vxz,
                                                                                                VYx, VYy, VYz,
                                                                                                weight, 
                                                                                                cogX, cogY, cogZ)
        self.runCommand()
        return

    def queueDefineTool(self,name, x, y, z, VXx, VXy, Vxz, VYx, VYy, VYz, weight, cogX, cogY, cogZ):
        self.commands.append("DefineTool(\"{}\",{},{},{},{},{},{},{},{},{},{},{},{},{});".format(name,
                                                                                                x, y, z,
                                                                                                VXx, VXy, Vxz,
                                                                                                VYx, VYy, VYz,
                                                                                                weight, 
                                                                                                cogX, cogY, cogZ))
        return

    def attachTool(self,name):
        self.command = "AttachTool(\"{}\");".format(name) 
        self.runCommand()
        return

    def queueAttachTool(self,name):
        self.commands.append("AttachTool(\"{}\");".format(name))
        return   

    def detachTool(self):
        self.command = "DetachTool();" 
        self.runCommand()
        return

    def queueDetachTool(self):
        self.commands.append("DetachTool();")
        return 

    def writeDigital(self,pin,on):
        self.command = "WriteDigital({},{});".format(pin,on) 
        self.runCommand()
        return 

    def queueWriteDigital(self,pin,on):
        self.commands.append("WriteDigital({},{});".format(pin,on))
        return

    def writeAnalog(self,pin,value):
        self.command = "WriteAnalog({},{});".format(pin,value) 
        self.runCommand()
        return

    def queueWriteAnalog(self,pin,value):
        self.commands.append("WriteAnalog({},{});".format(pin,value))
        return

    # def externalAxis (self,axisNumber, rxternalAxisInc):
    #     self.command = "ExternalAxis({},{});".format(axisNumber, rxternalAxisInc) 
    #     self.runCommand()
    #     return  
    
    # def externalAxisTo (self,axisNumber, rxternalAxisVal):
    #     self.command = "ExternalAxisTo({},{});".format(axisNumber, rxternalAxisVal) 
    #     self.runCommand()
    #     return