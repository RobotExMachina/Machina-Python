"""
A convinient class of objects to communicate with Machina Bridge
"""
import socket

class MachinaRobot (object):

	def __init__(self, address = "ws://127.0.0.1:6999/Bridge", debug = False):
		# init 
		self.commands = []
		self.address = address
		self.debug = debug

	async def sendToBridge(address= "", command):
        # generic fucntion to communicate with web

        if not isinstance(cmds, str) :
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


    def runCommands(cmds = ""):
    	if cmds == "":
    		cmds = self.commands

    	if not isinstance(cmds, list) : 
    		if isinstance(cmds, str) :
    			cmds = [cmds]
    		else:
        		raise ValueError("command must be a list of strings.")


	    for cmd in cmds:
	    	if not isinstance(cmd, str) :
        		raise ValueError("command must be an string object.")
	        try:
	            asyncio.get_event_loop().run_until_complete(sendToBridge(self.address,cmd))
	        except:
	            print ("FAIL: {}".format(cmd))
	    return 


	def move( xInc, yInc, zInc = 0):
		if self.debug:
			if not isinstance(xInc, float):
	        	raise ValueError("xInc must be a float object.")
	        if not isinstance(yInc, float):
	        	raise ValueError("yInc must be a float object.")
	        if not isinstance(zInc, float):
        		raise ValueError("zInc must be a float object.")

		self.commands = "Move({},{},{});".format(xInc, yInc, zInc) 
		self.runCommands()


	def moveTo (x,y,z):
		self.commands = "MoveTo({},{},{});".format(x, y, z) 
		self.runCommands()


	def transformTo(x,y,z,x0,x1,x2,y0,y1,y2):
		self.commands = "TransformTo({},{},{},{},{},{},{},{},{});".format(x,y,z,x0,x1,x2,y0,y1,y2) 
		self.runCommands()

	def rotate(x,y,z,angleInc):
		self.commands = "Rotate({},{},{},{});".format(x,y,z,angleInc) 
		self.runCommands()

	def rotateTo(x0,x1,x2,y0,y1,y2):
		self.commands = "RotateTo({},{},{},{},{},{});".format(x0,x1,x2,y0,y1,y2) 
		self.runCommands()

	def axes (j1,j2,j3,j4,j5,j6):
		self.commands = "Axes({},{},{},{},{},{});".format(j1,j2,j3,j4,j5,j6) 
		self.runCommands()

	def axesTo (j1,j2,j3,j4,j5,j6):
		self.commands = "AxesTo({},{},{},{},{},{});".format(j1,j2,j3,j4,j5,j6) 
		self.runCommands()	

	def speed(speedInc):
		self.commands = "Speed({});".format(speedInc) 
		self.runCommands()	

	def speedTo(speedVal):
		self.commands = "SpeedTo({});".format(speedVal) 
		self.runCommands()	

	def acceleration(accelerationInc):
		self.commands = "Acceleration({});".format(accelerationInc) 
		self.runCommands()	

	def accelerationTo(accelerationVal):
		self.commands = "AccelerationTo({});".format(accelerationVal) 
		self.runCommands()	  


	def rotationSpeed(rotationSpeedInc):
		self.commands = "RotationSpeed({});".format(rotationSpeedInc) 
		self.runCommands()	

	def rotationSpeedTo(rotationSpeedVal):
		self.commands = "RotationSpeedTo({});".format(rotationSpeedVal) 
		self.runCommands()	

	def jointSpeed(jointSpeedInc):
		self.commands = "JointSpeed({});".format(jointSpeedInc) 
		self.runCommands()	

	def jointSpeedTo(jointSpeedVal):
		self.commands = "JointSpeedTo({});".format(jointSpeedVal) 
		self.runCommands()	

	def jointAcceleration(jointAccelerationInc):
		self.commands = "JointAcceleration({});".format(jointAccelerationInc) 
		self.runCommands()	

	def jointAccelerationTo(jointAccelerationVal):
		self.commands = "JointAccelerationTo({});".format(jointAccelerationVal) 
		self.runCommands()	

	def precision(precisionInc):
		self.commands = "Precision({});".format(PrecisionInc) 
		self.runCommands()	

	def PrecisionTo(precisionVal):
		self.commands = "PrecisionTo({});".format(precisionVal) 
		self.runCommands()	

	def motionMode(mode):
		self.commands = "MotionMode(\"{}\");".format(mode) 
		self.runCommands()	

	def message(msg):
		self.commands = "Message(\"{}\");".format(msg) 
		self.runCommands()	

	def wait(millis):
		self.commands = "Wait({});".format(millis) 
		self.runCommands()	

	def pushSettings():
		self.commands = "PushSettings();" 
		self.runCommands()	

	def popSettings():
		self.commands = "PopSettings();" 
		self.runCommands()	

	def toolCreate(name, x, y, z, x0, x1, x2, y0, y1, y2, weight, cogX, cogY, cogZ):
		self.commands =   "Tool.create(\"{}\",{},{},{},{},{},{},{},{},{},{},{},{},{},);".format(name, 
																								x, y, z, 
																								x0, x1, x2, 
																								y0, y1, y2, 
																								weight, 
																								cogX, cogY, cogZ)
		self.runCommands()


	def attach(name):
		self.commands = "Attach(\"{}\");".format(name) 
		self.runCommands()	

	def detach():
		self.commands = "Detach()" 
		self.runCommands()	

	def writeDigital(pin,on):
		self.commands = "WriteDigital({},{});".format(pin,on) 
		self.runCommands()	

	def writeAnalog(pin,value):
		self.commands = "WriteAnalog({},{});".format(pin,value) 
		self.runCommands()	


a = MachinaRobot()


