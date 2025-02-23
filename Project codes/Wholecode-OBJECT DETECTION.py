import vrep
import time
import math

vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP
if clientID!=-1:
    print ('Connected to remote API server')
    vrep.simxAddStatusbarMessage(clientID,'Hello V-REP!',vrep.simx_opmode_oneshot)
    #HANDLES
    res,rightmotor=vrep.simxGetObjectHandle(clientID,'K3_rightWheelMotor',vrep.simx_opmode_blocking)
    res,leftmotor=vrep.simxGetObjectHandle(clientID,'K3_leftWheelMotor',vrep.simx_opmode_blocking)
    res,sensor1=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor1',vrep.simx_opmode_blocking)
    res,sensor2=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor2',vrep.simx_opmode_blocking)
    res,sensor3=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor3',vrep.simx_opmode_blocking)
    res,sensor4=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor4',vrep.simx_opmode_blocking)
    res,sensor5=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor5',vrep.simx_opmode_blocking)
    res,sensor6=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor6',vrep.simx_opmode_blocking)
    res,sensor7=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor7',vrep.simx_opmode_blocking)
    res,sensor8=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor8',vrep.simx_opmode_blocking)
    res,sensor9=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor9',vrep.simx_opmode_blocking)
    res,origin=vrep.simxGetObjectHandle(clientID,'Origin_R2',vrep.simx_opmode_blocking)
    res,wait=vrep.simxGetObjectHandle(clientID,'WaitArea',vrep.simx_opmode_blocking)
    res,goal1=vrep.simxGetObjectHandle(clientID,'Goal1',vrep.simx_opmode_blocking)
    res,goal2=vrep.simxGetObjectHandle(clientID,'Goal2',vrep.simx_opmode_blocking)
    res,goal3=vrep.simxGetObjectHandle(clientID,'Goal3',vrep.simx_opmode_blocking)
    res,object1=vrep.simxGetObjectHandle(clientID,'Object1',vrep.simx_opmode_blocking)
    res,object2=vrep.simxGetObjectHandle(clientID,'Object2',vrep.simx_opmode_blocking)
    res,object3=vrep.simxGetObjectHandle(clientID,'Object3',vrep.simx_opmode_blocking)
    res,robot=vrep.simxGetObjectHandle(clientID,'K3_robot',vrep.simx_opmode_blocking)
    res,s1=vrep.simxGetObjectHandle(clientID,'K3_colorSensorRight',vrep.simx_opmode_blocking)
    #STREAMING FUNCTIONS
    res,resolution,image=vrep.simxGetVisionSensorImage(clientID,s1,1,vrep.simx_opmode_streaming)
    res,oposition=vrep.simxGetObjectPosition(clientID,origin,-1,vrep.simx_opmode_streaming)
    res,wposition=vrep.simxGetObjectPosition(clientID,wait,-1,vrep.simx_opmode_streaming)
    res,g1position=vrep.simxGetObjectPosition(clientID,goal1,-1,vrep.simx_opmode_streaming)
    res,g2position=vrep.simxGetObjectPosition(clientID,goal2,-1,vrep.simx_opmode_streaming)
    res,g3position=vrep.simxGetObjectPosition(clientID,goal3,-1,vrep.simx_opmode_streaming)
    res,obj1position=vrep.simxGetObjectPosition(clientID,object1,-1,vrep.simx_opmode_streaming)
    res,obj2position=vrep.simxGetObjectPosition(clientID,object2,-1,vrep.simx_opmode_streaming)
    res,obj3position=vrep.simxGetObjectPosition(clientID,object3,-1,vrep.simx_opmode_streaming)
    res,rposition=vrep.simxGetObjectPosition(clientID,robot,-1,vrep.simx_opmode_streaming)
    res,eulerAngles=vrep.simxGetObjectOrientation(clientID,robot,-1,vrep.simx_opmode_streaming)
    res,detection1,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_streaming)
    res,detection2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_streaming)
    res,detection3,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor3,vrep.simx_opmode_streaming)
    res,detection4,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_streaming)
    res,detection5,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_streaming)
    res,detection6,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor6,vrep.simx_opmode_streaming)
    res,detection7,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor7,vrep.simx_opmode_streaming)
    res,detection8,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor8,vrep.simx_opmode_streaming)
    res,detection9,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor9,vrep.simx_opmode_streaming)
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
    #PRINTING SENSOR VALUES
    print(detection1)
    print(detection2)
    print(detection3)
    print(detection4)
    print(detection5)
    print(detection6)
    print(detection7)
    print(detection8)
    print(detection9)

############################################################GPS############################################################################
    res,oposition=vrep.simxGetObjectPosition(clientID,origin,-1,vrep.simx_opmode_buffer)
    res,wposition=vrep.simxGetObjectPosition(clientID,wait,-1,vrep.simx_opmode_buffer)
    res,g1position=vrep.simxGetObjectPosition(clientID,goal1,-1,vrep.simx_opmode_buffer)
    res,g2position=vrep.simxGetObjectPosition(clientID,goal2,-1,vrep.simx_opmode_buffer)
    res,g3position=vrep.simxGetObjectPosition(clientID,goal3,-1,vrep.simx_opmode_buffer)
    res,obj1position=vrep.simxGetObjectPosition(clientID,object1,-1,vrep.simx_opmode_buffer)
    res,obj2position=vrep.simxGetObjectPosition(clientID,object2,-1,vrep.simx_opmode_buffer)
    res,obj3position=vrep.simxGetObjectPosition(clientID,object3,-1,vrep.simx_opmode_buffer)
    res,rposition=vrep.simxGetObjectPosition(clientID,robot,-1,vrep.simx_opmode_buffer)
    res,eulerAngles=vrep.simxGetObjectOrientation(clientID,robot,-1,vrep.simx_opmode_buffer)
    yw = rposition[1]-wposition[1] #y2-y1
    yo = rposition[1]-oposition[1] #y2-y1
    y1 = rposition[1]-g1position[1] #y2-y1
    y2 = rposition[1]-g2position[1] #y2-y1
    y3 = rposition[1]-g3position[1] #y2-y1
    yobj1 = rposition[1]-obj1position[1] #y2-y1
    yobj2 = rposition[1]-obj2position[1] #y2-y1
    yobj3 = rposition[1]-obj3position[1] #y2-y1
    xw = rposition[0]-wposition[0] #x2-x1
    xo = rposition[0]-oposition[0] #x2-x1
    x1 = rposition[0]-g1position[0] #x2-x1
    x2 = rposition[0]-g2position[0] #x2-x1
    x3 = rposition[0]-g3position[0] #x2-x1
    xobj1 = rposition[0]-obj1position[0] #x2-x1
    xobj2 = rposition[0]-obj2position[0] #x2-x1
    xobj3 = rposition[0]-obj3position[0] #x2-x1
    Slopeanglew = math.atan2(yw,xw)*180/3.1415
    Slopeangleo = math.atan2(yo,xo)*180/3.1415
    Slopeangle1 = math.atan2(y1,x1)*180/3.1415
    Slopeangle2 = math.atan2(y2,x2)*180/3.1415
    Slopeangle3 = math.atan2(y3,x3)*180/3.1415
    Slopeangleobj1 = math.atan2(yobj1,xobj1)*180/3.1415
    Slopeangleobj2 = math.atan2(yobj2,xobj2)*180/3.1415
    Slopeangleobj3 = math.atan2(yobj3,xobj3)*180/3.1415
    
    if (Slopeanglew<0 and Slopeanglew<-90): #correction made to ensure angle remains between 0-90
       correctionw = -1*(180 +Slopeanglew)
    if (Slopeangleo<0 and Slopeangleo<-90): #correction made to ensure angle remains between 0-90
       correctiono = -1*(180 +Slopeangleo)
    if (Slopeangle1<0 and Slopeangle1<-90): #correction made to ensure angle remains between 0-90
       correction1 = -1*(180 +Slopeangle1) 
    if (Slopeangle2<0 and Slopeangle2<-90): #correction made to ensure angle remains between 0-90
       correction2 = -1*(180 +Slopeangle2)
    if (Slopeangle3<0 and Slopeangle3<-90): #correction made to ensure angle remains between 0-90
       correction3 = -1*(180 +Slopeangle3)        
    if (Slopeangleobj1<0 and Slopeangleobj1<-90): #correction made to ensure angle remains between 0-90
       correctionobj1 = -1*(180 +Slopeangleobj1)        
    if (Slopeangleobj2<0 and Slopeangleobj2<-90): #correction made to ensure angle remains between 0-90
       correctionobj2 = -1*(180 +Slopeangleobj2)        
    if (Slopeangleobj3<0 and Slopeangleobj3<-90): #correction made to ensure angle remains between 0-90
       correctionobj3 = -1*(180 +Slopeangleobj3)        
    if (Slopeanglew<0 and Slopeanglew>-90): #correction made void if angle is already less than 90
       correctionw=Slopeanglew
    if (Slopeangleo<0 and Slopeangleo>-90): #correction made void if angle is already less than 90
       correctiono=Slopeangleo
    if (Slopeangle1<0 and Slopeangle1>-90): #correction made void if angle is already less than 90
       correction1=Slopeangle1
    if (Slopeangle2<0 and Slopeangle2>-90): #correction made void if angle is already less than 90
       correction2=Slopeangle2
    if (Slopeangle3<0 and Slopeangle3>-90): #correction made void if angle is already less than 90
       correction3=Slopeangle3
    if (Slopeangleobj1<0 and Slopeangleobj1>-90): #correction made void if angle is already less than 90
       correctionobj1=Slopeangleobj1
    if (Slopeangleobj2<0 and Slopeangleobj2>-90): #correction made void if angle is already less than 90
       correctionobj2=Slopeangleobj2
    if (Slopeangleobj3<0 and Slopeangleobj3>-90): #correction made void if angle is already less than 90
       correctionobj3=Slopeangleobj3
       spw = correctionw + 1 #Range added to Slopeangle
       spo = correctiono + 1 #Range added to Slopeangle
    sp1 = correction1 + 1 #Range added to Slopeangle
    sp2 = correction2 + 1 #Range added to Slopeangle
    sp3 = correction3 + 1 #Range added to Slopeangle
    spobj1 = correctionobj1 + 1 #Range added to Slopeangle
    spobj2 = correctionobj2 + 1 #Range added to Slopeangle
    spobj3 = correctionobj3 + 1 #Range added to Slopeangle
    smw = correctionw - 1 #Range added to Slopeangle 
    smo = correctiono - 1 #Range added to Slopeangle 
    sm1= correction1 - 1 #Range added to Slopeangle 
    sm2 = correction2 - 1 #Range added to Slopeangle 
    sm3 = correction3 - 1 #Range added to Slopeangle 
    smobj1 = correctionobj1 - 1 #Range added to Slopeangle 
    smobj2 = correctionobj2 - 1 #Range added to Slopeangle 
    smobj3 = correctionobj3 - 1 #Range added to Slopeangle 
    rpw = correctionw + 10 #Range added to continue on path
    rpo = correctiono + 10 #Range added to continue on path
    rp1 = correction1 + 10 #Range added to continue on path
    rp2 = correction2 + 10 #Range added to continue on path
    rp3 = correction3 + 10 #Range added to continue on path
    rpobj1 = correctionobj1 + 10 #Range added to continue on path
    rpobj2 = correctionobj2 + 10 #Range added to continue on path
    rpobj3 = correctionobj3 + 10 #Range added to continue on path
    rmw = correctionw - 10 #Range added to continue on path
    rmo = correctiono - 10 #Range added to continue on path
    rm1 = correction1 - 10 #Range added to continue on path
    rm2 = correction2 - 10 #Range added to continue on path
    rm3 = correction3 - 10 #Range added to continue on path
    rmobj1 = correctionobj1 - 10 #Range added to continue on path
    rmobj2 = correctionobj2 - 10 #Range added to continue on path
    rmobj3 = correctionobj3 - 10 #Range added to continue on path


    inval = 5
    
    if (inval == 0):#inval 0 Robot1 will move to waiting area
        sp=spw
        sm=smw
        rp=rpw
        rm=rmw
        Slopeangle = Slopeanglew
    elif(inval == 1): #inval 1 When R2 sends R1 inval 1 it will move to goal1
            sp=sp1
            sm=sm1
            rp=rp1
            rm=rm1
            Slopeangle = Slopeangle1
    elif(inval == 2): #inval 2 When R2 sends R1 inval 2 it will move to goal2
            sp=sp2
            sm=sm2
            rp=rp2
            rm=rm2
            Slopeangle = Slopeangle2
    elif(inval == 3): #inval 3 When R2 sends R1 inval 3 it will move to goal3
            sp=sp3
            sm=sm3
            rp=rp3
            rm=rm3
            Slopeangle = Slopeangle3
    elif(inval == 4): #inval 4 When R2 sends R1 inval it will move to its Origin_R2
            sp=spo
            sm=smo
            rp=rpo
            rm=rmo
            Slopeangle = Slopeangleo
    elif(inval == 5): #inval 1 When R2 sends R1 inval 1 it will move to goal1
            sp=spobj1
            sm=smobj1
            rp=rpobj1
            rm=rmobj1
            Slopeangle = Slopeangleobj1
    elif(inval == 6): #inval 2 When R2 sends R1 inval 2 it will move to goal2
            sp=spobj2
            sm=smobj2
            rp=rpobj2
            rm=rmobj2
            Slopeangle = Slopeangleobj2
    elif(inval == 7): #inval 3 When R2 sends R1 inval 3 it will move to goal3
            sp=spobj3
            sm=smobj3
            rp=rpobj3
            rm=rmobj3
            Slopeangle = Slopeangleobj3
    wx =0.05 #X Positon of Goal
    ox = -1.5
    g1x = -1.125
    g2x = 0.1
    g3x = 0.92
    obj1x = -0.5312
    obj2x = -0.1562
    obj3x = 0.2438
    wxx = 0.3    
    oxx = -1.35
    g1xx = -0.8
    g2xx = 0.25
    g3xx = 1.28
    obj1xx = -0.35
    obj2xx = 0.06
    obj3xx = 0.4688
    wy = 1.1 #Y Position of Goal   
    oy = 1.25
    g1y = 1.95
    g2y = 1.95
    g3y = 1.95
    obj1y = -1.1539
    obj2y = -1.1539
    obj3y = -1.1539
    wyy= 1.3    
    oyy = 1.4
    g1yy = 2.2
    g2yy = 2.2
    g3yy = 2.2
    obj1yy = -0.75
    obj1yy = -0.75
    obj1yy = -0.75
    Alpha=eulerAngles[0]*57.3 #Euler Angles
    Beta=eulerAngles[1]*57.3 #Euler Angles
    Gamma=eulerAngles[2]*57.3 #Euler Angles
#################PRINT###################
    #print (Alpha)
    #print (Beta)
    #print (Gamma)
    #print (y)
    #print (x)
    #print(image)
    print (Slopeanglew)
    #print (correction)
    #print (robot 0)
######################################### STOP_AT_GOAL ################################################################## 			
    if (inval==0 and rposition[0]>=wx and rposition[0]<=wxx and rposition[1]>=wy and rposition[1]<=wyy):#stop khepera at WaitArea
       res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,0.00,vrep.simx_opmode_streaming) #set velocity of left motor
       res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,0.00,vrep.simx_opmode_streaming) #set velocity of right motor
       time.sleep(60)
    if (inval==4 and rposition[0]>=ox and rposition[0]<=oxx and rposition[1]>=oy and rposition[1]<=oyy):#stop khepera at Origin_R2
       res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,0.00,vrep.simx_opmode_streaming) #set velocity of left motor
       res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,0.00,vrep.simx_opmode_streaming) #set velocity of right motor
       time.sleep(60)
    if (inval==1 and rposition[0]>=g1x and rposition[0]<=g1xx and rposition[1]>=g1y and rposition[1]<=g1yy):#stop khepera at goal1
       res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,0.00,vrep.simx_opmode_streaming) #set velocity of left motor
       res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,0.00,vrep.simx_opmode_streaming) #set velocity of right motor
       time.sleep(60)
    if (inval==2 and rposition[0]>=g2x and rposition[0]<=g2xx and rposition[1]>=g2y and rposition[1]<=g2yy):#stop khepera at goal2
       res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,0.00,vrep.simx_opmode_streaming) #set velocity of left motor
       res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,0.00,vrep.simx_opmode_streaming) #set velocity of right motor
       time.sleep(60)
    if (inval==3 and rposition[0]>=g3x and rposition[0]<=g3xx and rposition[1]>=g3y and rposition[1]<=g3yy):#stop khepera at goal3
       res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,0.00,vrep.simx_opmode_streaming) #set velocity of left motor
       res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,0.00,vrep.simx_opmode_streaming) #set velocity of right motor
       time.sleep(60)
    if (inval==5 and 95 in image):#rposition[0]>=obj1x and rposition[0]<=obj1xx and rposition[1]>=obj1y and rposition[1]<=obj1yy and 66 in image):#stop khepera at Object1
       res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,0.00,vrep.simx_opmode_streaming) #set velocity of left motor
       res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,0.00,vrep.simx_opmode_streaming) #set velocity of right motor
       time.sleep(60)
    if (inval==6 and 71 in image):#rposition[0]>=obj2x and rposition[0]<=obj2xx and rposition[1]>=obj2y and rposition[1]<=obj2yy and 44 in image):#stop khepera at Object1
       res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,0.00,vrep.simx_opmode_streaming) #set velocity of left motor
       res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,0.00,vrep.simx_opmode_streaming) #set velocity of right motor
       time.sleep(60)
    if (inval==7 and 81 in image):#rposition[0]>=obj3x and rposition[0]<=obj3xx and rposition[1]>=obj3y and rposition[1]<=obj3yy and 53 in image):#stop khepera at Object1
       res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,0.00,vrep.simx_opmode_streaming) #set velocity of left motor
       res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,0.00,vrep.simx_opmode_streaming) #set velocity of right motor
       time.sleep(60)

###########################################################OBS_A############################################################################
    elif((detection3==1) or (detection4==1)):
              res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,2.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,-2.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res,detection3,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor3,vrep.simx_opmode_buffer)
              res,detection4,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_buffer)
    elif (detection5==1):
              res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,-2.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,2.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res,detection5,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_buffer)
    elif (detection2==1):
              res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,2.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,-2.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res,detection2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_buffer)
    elif((detection1==0) and (detection2==0) and (detection3==0) and (detection4==0) and ((detection5==0) or (detection6==0))):
              res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,2.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,2.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res,detection1,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_buffer)
              res,detection2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_buffer)
              res,detection3,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor3,vrep.simx_opmode_buffer)
              res,detection4,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_buffer)
              res,detection5,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_buffer)
              res,detection6,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor6,vrep.simx_opmode_buffer)
    elif(((detection1==1) or (detection2==1)) and (detection3==0) and (detection4==0) and (detection5==0) and (detection6==0)):
              res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,2.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,2.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res,detection1,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_buffer)
              res,detection2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_buffer)
              res,detection3,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor3,vrep.simx_opmode_buffer)
              res,detection4,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_buffer)
              res,detection5,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_buffer)
              res,detection6,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor6,vrep.simx_opmode_buffer)
############################################################GPS############################################################################
    if  (Slopeangle<1 and Slopeangle<-90 and Alpha<0 and Gamma<0 and Beta<0 and (sp>=Beta or Beta>=sm) and rposition[0]<0 and ((detection1==0) and (detection2==0) and (detection3==0) and (detection4==0) and (detection5==0) and (detection6==0) or (detection3==1) and (detection5==1)  or ((detection7==1) or (detection8==1) or (detection9==1)))): #Align Khepera in 2nd and 3rd Quaderant with angle greater than 90
              res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,2.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,2.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res,detection1,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_buffer)
              res,detection2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_buffer)
              res,detection3,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor3,vrep.simx_opmode_buffer)
              res,detection4,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_buffer)
              res,detection5,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_buffer)
              res,detection6,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor6,vrep.simx_opmode_buffer)
              res,detection7,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor7,vrep.simx_opmode_buffer)
              res,detection8,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor8,vrep.simx_opmode_buffer)
              res,detection9,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor9,vrep.simx_opmode_buffer)
    if (Beta<0 and (sp>=Beta or Beta>=sm) and Slopeangle>-90 and Alpha<0 and Gamma<0 and rposition[0]<0 and ((detection1==0) and (detection2==0) and (detection3==0) and (detection4==0) and (detection5==0) and (detection6==0) or (detection3==1) and (detection5==1)  or ((detection7==1) or (detection8==1) or (detection9==1)))): #Align Khepera in 2nd and 3rd Quaderant with angle less than 90
              res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,2.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,2.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res,detection1,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_buffer)
              res,detection2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_buffer)
              res,detection3,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor3,vrep.simx_opmode_buffer)
              res,detection4,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_buffer)
              res,detection5,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_buffer)
              res,detection6,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor6,vrep.simx_opmode_buffer)
              res,detection7,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor7,vrep.simx_opmode_buffer)
              res,detection8,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor8,vrep.simx_opmode_buffer)
              res,detection9,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor9,vrep.simx_opmode_buffer)
    if (Beta<0 and (sp>=Beta or Beta>=sm) and Slopeangle>-90 and Alpha>0 and Gamma>0 and rposition[0]>0 and ((detection1==0) and (detection2==0) and (detection3==0) and (detection4==0) and (detection5==0) and (detection6==0) or (detection3==1) and (detection5==1)  or ((detection7==1) or (detection8==1) or (detection9==1)))): #Align Khepera in 1st and 4th Quaderant with angle less than 90
              res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,2.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,2.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res,detection1,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_buffer)
              res,detection2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_buffer)
              res,detection3,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor3,vrep.simx_opmode_buffer)
              res,detection4,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_buffer)
              res,detection5,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_buffer)
              res,detection6,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor6,vrep.simx_opmode_buffer)
              res,detection7,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor7,vrep.simx_opmode_buffer)
              res,detection8,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor8,vrep.simx_opmode_buffer)
              res,detection9,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor9,vrep.simx_opmode_buffer)
    if (rposition[0]<0 and (rp<Beta or Beta<rm) and ((detection1==0) and (detection2==0) and (detection3==0) and (detection4==0) and (detection5==0) and (detection6==0) or (detection3==1) and (detection5==1) or ((detection7==1) or (detection8==1) or (detection9==1)))): #Turning Anticlockwise in 2nd and 3rd Quaderent
              res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,1.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,-1.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res,detection1,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_buffer)
              res,detection2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_buffer)
              res,detection3,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor3,vrep.simx_opmode_buffer)
              res,detection4,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_buffer)
              res,detection5,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_buffer)
              res,detection6,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor6,vrep.simx_opmode_buffer)
              res,detection7,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor7,vrep.simx_opmode_buffer)
              res,detection8,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor8,vrep.simx_opmode_buffer)
              res,detection9,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor9,vrep.simx_opmode_buffer)
    if (rposition[0]>0 and (rp<Beta or Beta<rm) and ((detection1==0) and (detection2==0) and (detection3==0) and (detection4==0) and (detection5==0) and (detection6==0) or (detection3==1) and (detection5==1)  or ((detection7==1) or (detection8==1) or (detection9==1)))): #Turning Clockwise in 1st and 4th Quaderent
              res=vrep.simxSetJointTargetVelocity(clientID,leftmotor, 1.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res=vrep.simxSetJointTargetVelocity(clientID,rightmotor, -1.00,vrep.simx_opmode_streaming) #set velocity of left motor
              res,detection1,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_buffer)
              res,detection2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_buffer)
              res,detection3,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor3,vrep.simx_opmode_buffer)
              res,detection4,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_buffer)
              res,detection5,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_buffer)
              res,detection6,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor6,vrep.simx_opmode_buffer)
              res,detection7,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor7,vrep.simx_opmode_buffer)
              res,detection8,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor8,vrep.simx_opmode_buffer)
              res,detection9,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor9,vrep.simx_opmode_buffer)

