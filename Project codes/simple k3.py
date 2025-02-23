import vrep
import time
import math
    
    
def k ():
    vrep.simxFinish(-1) # just in case, close all opened connections
    clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP
    if clientID!=-1:
        print ('Connected to remote API server')
        vrep.simxAddStatusbarMessage(clientID,'Hello V-REP!',vrep.simx_opmode_oneshot)
        #HANDLES
        res,rightmotor1=vrep.simxGetObjectHandle(clientID,'K3_rightWheelMotor#0',vrep.simx_opmode_blocking)
        res,leftmotor1=vrep.simxGetObjectHandle(clientID,'K3_leftWheelMotor#0',vrep.simx_opmode_blocking)
        res,sensor1=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor1#0',vrep.simx_opmode_blocking)
        res,sensor2=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor2#0',vrep.simx_opmode_blocking)
        res,sensor3=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor3#0',vrep.simx_opmode_blocking)
        res,sensor4=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor4#0',vrep.simx_opmode_blocking)
        res,sensor5=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor5#0',vrep.simx_opmode_blocking)
        res,sensor6=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor6#0',vrep.simx_opmode_blocking)
        res,sensor7=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor7#0',vrep.simx_opmode_blocking)
        res,sensor8=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor8#0',vrep.simx_opmode_blocking)
        res,sensor9=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor9#0',vrep.simx_opmode_blocking)
        res,gps=vrep.simxGetObjectHandle(clientID,'GPS',vrep.simx_opmode_blocking)
     #   res,gpsY=vrep.simxGetObjectHandle(clientID,'K3_GPSY',vrep.simx_opmode_blocking)
      #  res,gpsZ=vrep.simxGetObjectHandle(clientID,'K3_GPSZ',vrep.simx_opmode_blocking)
        res,s1=vrep.simxGetObjectHandle(clientID,'K3_colorSensorRight#0',vrep.simx_opmode_blocking)
        res,s2=vrep.simxGetObjectHandle(clientID,'K3_colorSensorRight#1',vrep.simx_opmode_blocking)
        res,s3=vrep.simxGetObjectHandle(clientID,'K3_colorSensorRight',vrep.simx_opmode_blocking)
        res,s4=vrep.simxGetObjectHandle(clientID,'K3_colorSensorRight#2',vrep.simx_opmode_blocking)
        res,robot=vrep.simxGetObjectHandle(clientID,'K3_robot',vrep.simx_opmode_blocking)
        res,robot1=vrep.simxGetObjectHandle(clientID,'RR',vrep.simx_opmode_blocking)
        res,robot2=vrep.simxGetObjectHandle(clientID,'K3_robot#0',vrep.simx_opmode_blocking)
        res,robot3=vrep.simxGetObjectHandle(clientID,'K3_robot#1',vrep.simx_opmode_blocking)
       
        
        #STREAMING FUNCTIONS
      
        res,detection1,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_streaming)
        res,detection2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_streaming)
        res,detection3,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor3,vrep.simx_opmode_streaming)
        res,detection4,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_streaming)
        res,detection5,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_streaming)
        res,detection6,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor6,vrep.simx_opmode_streaming)
        res,detection7,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor7,vrep.simx_opmode_streaming)
        res,detection8,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor8,vrep.simx_opmode_streaming)
        res,detection9,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor9,vrep.simx_opmode_streaming)
        res,resolution,image=vrep.simxGetVisionSensorImage(clientID,s1,1,vrep.simx_opmode_streaming)
        res,resolution,image3=vrep.simxGetVisionSensorImage(clientID,s3,1,vrep.simx_opmode_streaming)
        res,resolution,image4=vrep.simxGetVisionSensorImage(clientID,s4,1,vrep.simx_opmode_streaming)
        res,resolution,image2=vrep.simxGetVisionSensorImage(clientID,s2,1,vrep.simx_opmode_streaming)
        wposition1=vrep.simxGetObjectPosition(clientID,robot,-1,vrep.simx_opmode_streaming)
        rposition1=vrep.simxGetObjectPosition(clientID,robot1,-1,vrep.simx_opmode_streaming)
        vposition1=vrep.simxGetObjectPosition(clientID,robot2,-1,vrep.simx_opmode_streaming)
        uposition1=vrep.simxGetObjectPosition(clientID,robot3,-1,vrep.simx_opmode_streaming)
        
       # res=vrep.simxSetFloatSignal(clientID,'K3_robot',objectAbsolutePosition,vrep.simx_opmode_streaming)
        
    else:
        print ('Failed connecting to remote API server')
        print ('Program ended')

    while clientID!=-1:
        #BUFFER
        res,detection1,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_buffer)
        res,detection2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_buffer)
        res,detection3,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor3,vrep.simx_opmode_buffer)
        res,detection4,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_buffer)
        res,detection5,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_buffer)
        res,detection6,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor6,vrep.simx_opmode_buffer)
        res,detection7,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor7,vrep.simx_opmode_buffer)
        res,detection8,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor8,vrep.simx_opmode_buffer)
        res,detection9,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor9,vrep.simx_opmode_buffer)
        res,resolution,image=vrep.simxGetVisionSensorImage(clientID,s1,1,vrep.simx_opmode_buffer)
        res,resolution,image3=vrep.simxGetVisionSensorImage(clientID,s3,1,vrep.simx_opmode_buffer)
        res,resolution,image2=vrep.simxGetVisionSensorImage(clientID,s2,1,vrep.simx_opmode_buffer)
        res,resolution,image4=vrep.simxGetVisionSensorImage(clientID,s4,1,vrep.simx_opmode_buffer)
        wposition1=vrep.simxGetObjectPosition(clientID,robot,-1,vrep.simx_opmode_buffer)
        rposition1=vrep.simxGetObjectPosition(clientID,robot1,-1,vrep.simx_opmode_buffer)
        vposition1=vrep.simxGetObjectPosition(clientID,robot2,-1,vrep.simx_opmode_buffer)
        uposition1=vrep.simxGetObjectPosition(clientID,robot3,-1,vrep.simx_opmode_buffer)
        #PRINTING SENSOR VALUES
        #print(detection1)
        #print(detection2)
        #print(detection3)
        #print(detection4)
        #print(detection5)
        #print(detection6)
        #print(detection7)
        #print(detection8)
        #print(detection9)
#        a=objectAbsolutePosition[1]
##        x=a[0]
##        y=a[1]
##        z=a[2]
        
        #str=vrep.simxPackFloats(a)
        #res=vrep.simxSetStringSignal(clientID,'coordinates',str,vrep.simx_opmode_oneshot)
       # print ("x= ",x , "y= ",y , "z= " ,z)
       # print (a)
        rposition=rposition1[1]
        wposition=wposition1[1]
        vposition=vposition1[1]
        uposition=uposition1[1]
     #####################################################################
        
        x3=vposition[0]
        y3=vposition[1]

        x4=uposition[0]
        y4=uposition[1] 

    
        
        ########################
        x2=rposition[0]
        y2=rposition[1]
        x1=wposition[0]
        y1=wposition[1]

       
        i=image[1]

        
        ##################################
        xv = x3-x1 #x2-x1
        yv = y3-y1 #y2-y1 
    
        xw = x2-x1 #x2-x1
        yw = y2-y1 #y2-y1


        xu = x4-x1 #x2-x1
        yu = y4-y1 #y2-y1  

        sq1 = (x1-x2)*(x1-x2)
        sq2 = (y1-y2)*(y1-y2)
        d1=math.sqrt(sq1 + sq2)
        
        ###############################
        sq3 = (x1-x3)*(x1-x3)
        sq4 = (y1-y3)*(y1-y3)
        d2=math.sqrt(sq3 + sq4)
        #################################

        sq5 = (x1-x4)*(x1-x4)
        sq6 = (y1-y4)*(y1-y4)
        d3= math.sqrt(sq5 + sq6)
        
        #################PRINT###################
        #print (Alpha)
        #print (Beta)
        #print (Gamma)
        #print (y)
        #print (x)
        #print (Slopeangle)
        #print (correction)
        #print (robot 0)
        print (image)
       #################################################################################################################################
    

                
###############################################################################################################################                
           
                 # res=vrep.simxStopSimulation(clientID,vrep.simx_opmode_oneshot)
        
           
        ###########################################################OBS_A############################################################################
        if((detection3==1) or (detection4==1)):
            res=vrep.simxSetJointTargetVelocity(clientID,leftmotor1,2.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res=vrep.simxSetJointTargetVelocity(clientID,rightmotor1,-2.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res,detection3,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor3,vrep.simx_opmode_buffer)
            res,detection4,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_buffer)
        elif (detection5==1):
            res=vrep.simxSetJointTargetVelocity(clientID,leftmotor1,-2.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res=vrep.simxSetJointTargetVelocity(clientID,rightmotor1,2.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res,detection5,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_buffer)
        elif (detection2==1):
            res=vrep.simxSetJointTargetVelocity(clientID,leftmotor1,2.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res=vrep.simxSetJointTargetVelocity(clientID,rightmotor1,-2.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res,detection2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_buffer)
        elif((detection1==0) and (detection2==0) and (detection3==0) and (detection4==0) and ((detection5==0) or (detection6==0))):
            res=vrep.simxSetJointTargetVelocity(clientID,leftmotor1,4.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res=vrep.simxSetJointTargetVelocity(clientID,rightmotor1,4.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res,detection1,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_buffer)
            res,detection2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_buffer)
            res,detection3,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor3,vrep.simx_opmode_buffer)
            res,detection4,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_buffer)
            res,detection5,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_buffer)
            res,detection6,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor6,vrep.simx_opmode_buffer)
        elif(((detection1==1) or (detection2==1)) and (detection3==0) and (detection4==0) and (detection5==0) and (detection6==0)):
            res=vrep.simxSetJointTargetVelocity(clientID,leftmotor1,4.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res=vrep.simxSetJointTargetVelocity(clientID,rightmotor1,4.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res,detection1,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_buffer)
            res,detection2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_buffer)
            res,detection3,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor3,vrep.simx_opmode_buffer)
            res,detection4,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_buffer)
            res,detection5,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_buffer)
            res,detection6,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor6,vrep.simx_opmode_buffer)
          
k()
