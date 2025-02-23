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
        res,rightmotor1=vrep.simxGetObjectHandle(clientID,'K3_rightWheelMotor',vrep.simx_opmode_blocking)
        res,leftmotor1=vrep.simxGetObjectHandle(clientID,'K3_leftWheelMotor',vrep.simx_opmode_blocking)
        res,sensor1=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor1',vrep.simx_opmode_blocking)
        res,sensor2=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor2',vrep.simx_opmode_blocking)
        res,sensor3=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor3',vrep.simx_opmode_blocking)
        res,sensor4=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor4',vrep.simx_opmode_blocking)
        res,sensor5=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor5',vrep.simx_opmode_blocking)
        res,sensor6=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor6',vrep.simx_opmode_blocking)
        res,sensor7=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor7',vrep.simx_opmode_blocking)
        res,sensor8=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor8',vrep.simx_opmode_blocking)
        res,sensor9=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor9',vrep.simx_opmode_blocking)
        res,q1=vrep.simxGetObjectHandle(clientID,'K3_Battery#0',vrep.simx_opmode_blocking)
        res,q3=vrep.simxGetObjectHandle(clientID,'K3_Battery#2',vrep.simx_opmode_blocking)
        res,q2=vrep.simxGetObjectHandle(clientID,'K3_Battery#1',vrep.simx_opmode_blocking)
        res,r1=vrep.simxGetObjectHandle(clientID,'K3_Aresource#0',vrep.simx_opmode_blocking)
        res,r3=vrep.simxGetObjectHandle(clientID,'K3_Aresource#2',vrep.simx_opmode_blocking)
        res,r2=vrep.simxGetObjectHandle(clientID,'K3_Aresource#1',vrep.simx_opmode_blocking)
        res,v1=vrep.simxGetObjectHandle(clientID,'K3_Cvelocity#0',vrep.simx_opmode_blocking)
        res,v3=vrep.simxGetObjectHandle(clientID,'K3_Cvelocity#2',vrep.simx_opmode_blocking)
        res,v2=vrep.simxGetObjectHandle(clientID,'K3_Cvelocity#1',vrep.simx_opmode_blocking)        
        res,s1=vrep.simxGetObjectHandle(clientID,'K3_Apriority#0',vrep.simx_opmode_blocking)
        res,s2=vrep.simxGetObjectHandle(clientID,'K3_Apriority#1',vrep.simx_opmode_blocking)
        res,s3=vrep.simxGetObjectHandle(clientID,'K3_colorSensorRight',vrep.simx_opmode_blocking)
        res,sR=vrep.simxGetObjectHandle(clientID,'K3_Apriority',vrep.simx_opmode_blocking)
        res,s4=vrep.simxGetObjectHandle(clientID,'K3_Apriority#2',vrep.simx_opmode_blocking)
        res,robot1=vrep.simxGetObjectHandle(clientID,'K3_robot',vrep.simx_opmode_blocking)
        res,robot=vrep.simxGetObjectHandle(clientID,'RR',vrep.simx_opmode_blocking)
        res,robot2=vrep.simxGetObjectHandle(clientID,'K3_robot#0',vrep.simx_opmode_blocking)
        res,robot3=vrep.simxGetObjectHandle(clientID,'K3_robot#1',vrep.simx_opmode_blocking)
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
        res,resolution,left2=vrep.simxGetVisionSensorImage(clientID,q2,1,vrep.simx_opmode_streaming)
        res,resolution,left1=vrep.simxGetVisionSensorImage(clientID,q1,1,vrep.simx_opmode_streaming)
        res,resolution,left3=vrep.simxGetVisionSensorImage(clientID,q3,1,vrep.simx_opmode_streaming)
        res,resolution,res2=vrep.simxGetVisionSensorImage(clientID,r2,1,vrep.simx_opmode_streaming)
        res,resolution,res1=vrep.simxGetVisionSensorImage(clientID,r1,1,vrep.simx_opmode_streaming)
        res,resolution,res3=vrep.simxGetVisionSensorImage(clientID,r3,1,vrep.simx_opmode_streaming)        
        res,resolution,vel2=vrep.simxGetVisionSensorImage(clientID,v2,1,vrep.simx_opmode_streaming)
        res,resolution,vel1=vrep.simxGetVisionSensorImage(clientID,v1,1,vrep.simx_opmode_streaming)
        res,resolution,vel3=vrep.simxGetVisionSensorImage(clientID,v3,1,vrep.simx_opmode_streaming)
        res,resolution,Rpriority=vrep.simxGetVisionSensorImage(clientID,sR,1,vrep.simx_opmode_streaming)
        wposition1=vrep.simxGetObjectPosition(clientID,robot,-1,vrep.simx_opmode_streaming)
        rposition1=vrep.simxGetObjectPosition(clientID,robot1,-1,vrep.simx_opmode_streaming)
        vposition1=vrep.simxGetObjectPosition(clientID,robot2,-1,vrep.simx_opmode_streaming)
        uposition1=vrep.simxGetObjectPosition(clientID,robot3,-1,vrep.simx_opmode_streaming)
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
        res,resolution,left2=vrep.simxGetVisionSensorImage(clientID,q2,1,vrep.simx_opmode_buffer)
        res,resolution,left1=vrep.simxGetVisionSensorImage(clientID,q1,1,vrep.simx_opmode_buffer)
        res,resolution,left3=vrep.simxGetVisionSensorImage(clientID,q3,1,vrep.simx_opmode_buffer)
        res,resolution,res2=vrep.simxGetVisionSensorImage(clientID,r2,1,vrep.simx_opmode_buffer)
        res,resolution,res1=vrep.simxGetVisionSensorImage(clientID,r1,1,vrep.simx_opmode_buffer)
        res,resolution,res3=vrep.simxGetVisionSensorImage(clientID,r3,1,vrep.simx_opmode_buffer)
        res,resolution,vel2=vrep.simxGetVisionSensorImage(clientID,v2,1,vrep.simx_opmode_buffer)
        res,resolution,vel1=vrep.simxGetVisionSensorImage(clientID,v1,1,vrep.simx_opmode_buffer)
        res,resolution,vel3=vrep.simxGetVisionSensorImage(clientID,v3,1,vrep.simx_opmode_buffer)        
        res,resolution,Rpriority=vrep.simxGetVisionSensorImage(clientID,sR,1,vrep.simx_opmode_buffer)
        wposition1=vrep.simxGetObjectPosition(clientID,robot,-1,vrep.simx_opmode_buffer)
        rposition1=vrep.simxGetObjectPosition(clientID,robot1,-1,vrep.simx_opmode_buffer)
        vposition1=vrep.simxGetObjectPosition(clientID,robot2,-1,vrep.simx_opmode_buffer)
        uposition1=vrep.simxGetObjectPosition(clientID,robot3,-1,vrep.simx_opmode_buffer)
        rposition=rposition1[1]
        wposition=wposition1[1]
        vposition=vposition1[1]
        uposition=uposition1[1]
        x3=vposition[0]
        y3=vposition[1]
        x4=uposition[0]
        y4=uposition[1] 
        x2=rposition[0]
        y2=rposition[1]
        x1=wposition[0]
        y1=wposition[1]
        xv = x3-x1 #x2-x1
        yv = y3-y1 #y2-y1     
        xw = x2-x1 #x2-x1
        yw = y2-y1 #y2-y1
        xu = x4-x1 #x2-x1
        yu = y4-y1 #y2-y1  
        sq1 = (x1-x2)*(x1-x2)
        sq2 = (y1-y2)*(y1-y2)
        d1=math.sqrt(sq1 + sq2)
        sq3 = (x1-x3)*(x1-x3)
        sq4 = (y1-y3)*(y1-y3)
        d2=math.sqrt(sq3 + sq4)
        sq5 = (x1-x4)*(x1-x4)
        sq6 = (y1-y4)*(y1-y4)
        d3= math.sqrt(sq5 + sq6)
            ###priority###
        if (46 in image4 ):
            p4=50
        if (0 in image4 ):
            p4=0
        if (17 in image4 ):
            p4=20            
        if (85 in image4 ):
            p4=100
                                          
        if (66 in image4):
            p4=70
        if (46 in image):
            p=50
        if (0 in image ):
            p=0
        if (17 in image ):
            p=20                        
        if (66 in image):
            p=70
        if (85 in image):
            p=100
        if (46 in image2):
            p2=50
        if (0 in image2):
            p2=0
        if (17 in image2):
            p2=20                  
        if (66 in image2):
            p2=70
        if (85 in image2):
            p2=100            
##################BATTERY######################################                             
        if (46 in left3):            
            b3=40
        if (85 in left3):            
            b3=80            
        if (66 in left3):
            b3=60
        if (17 in left3):
            b3=20 
        if (46 in left1):
            b=40
        if (66 in left1):
            b=60
        if (17 in left1):
            b=20
        if (85 in left1):
            b=80             
        if (46 in left2):
            b2=40
        if (66 in left2):            
            b2=60
        if (85 in left2):
            b2=80            
        if (17 in left2):
            b2=20
#############Rpriority###########################
        if (46 in Rpriority ):
            Rp=50
        if (0 in Rpriority ):
            Rp=0
        if (17 in Rpriority):
            Rp=20            
        if (85 in Rpriority ):
            Rp=100                                          
        if (66 in Rpriority):
            Rp=70
#################velocity##################################
        if (46 in vel3):            
            v3=30
        if (0 in vel3):            
            v3=0            
        if (85 in vel3):
            v3=50            
        if (66 in vel3):
            b3=40
        if (17 in vel3):
            v3=20 
        if (46 in vel1):
            v=30
        if (66 in vel1):
            v=40
        if (17 in vel1):
            v=20
        if (0 in vel1):
            v=0
        if (85 in vel1):
            v=50             
        if (46 in vel2):
            v2=30
        if (66 in vel2):            
            v2=40
        if (85 in vel2):
            v2=50
        if (0 in vel2):
            b2=0            
        if (17 in vel2):
            v2=20                                  
        if (46 in image3):#camera
            if(46 in res1 and 46 in res2 and 46 in res3): 
                print ("BIDDING PROCESSING" )
                time.sleep(2)              
                cost2=b+v-d1-p 
                cost3=b2+v2-d2-p2          
                cost4=b3+v3-d3-p4       
                print ("cost4 = " , cost4)
                print ('cost2 = ' , cost2)
                print ('cost3 = ' , cost3)
                time.sleep(2)
                if(cost3>cost4 and cost4>cost2):
                    vrep.simxAddStatusbarMessage(clientID,'K3_ROBOT#0 IS COMING',vrep.simx_opmode_oneshot)
                    print ("K3_ROBOT#0 IS COMING" )
                    m()
                if(cost4>cost2 and cost2>cost3):
                    vrep.simxAddStatusbarMessage(clientID,'K3_ROBOT#1 IS COMING',vrep.simx_opmode_oneshot)
                    print ("K3_ROBOT#1 IS COMING" )
                    l()
                if(cost4>cost3 and cost3>cost2):
                    vrep.simxAddStatusbarMessage(clientID,'K3_ROBOT#1 IS COMING',vrep.simx_opmode_oneshot)
                    print ("K3_ROBOT#1 IS COMING" )
                    l()
                if(cost2>cost3 and cost3>cost4):
                    vrep.simxAddStatusbarMessage(clientID,'K3_ROBOT IS COMING',vrep.simx_opmode_oneshot)
                    print ("K3_ROBOT IS COMING" )
                    j()
                if(cost2>cost4 and cost4>cost3):
                    vrep.simxAddStatusbarMessage(clientID,'K3_ROBOT IS COMING',vrep.simx_opmode_oneshot)
                    print ("K3_ROBOT IS COMING" )
                    j()
                if(cost3>cost2 and cost2>cost4):
                    vrep.simxAddStatusbarMessage(clientID,'K3_ROBOT#0 IS COMING',vrep.simx_opmode_oneshot)
                    print ("K3_ROBOT#0 IS COMING" )
                    m()
            cost2=b+v-d1-p 
            cost3=b2+v2-d2-p2          
            cost4=b3+v3-d3-p4 
            if(46 in res1 and 46 in res2 and 0 in res3):
                print ("BIDDING PROCESSING AMONG K3_ROBOT AND K3_ROBOT#0  " )
                time.sleep(2)
                print ('cost2 FOR K3_ROBOT  = ' , cost2)
                print ('cost3 FOR K3_ROBOT#0 = ' , cost3)
                time.sleep(2)
                if(cost2>cost3):
                    print ("K3_ROBOT IS COMING" )
                    j()
                if(cost3>cost2):
                    print ("K3_ROBOT#0 IS COMING" )
                    m()                                        
            if(46 in res1 and 0 in res2 and 46 in res3):
                print ("BIDDING PROCESSING AMONG K3_ROBOT AND K3_ROBOT#1" )
                time.sleep(2)
                print ('cost2 FOR K3_ROBOT = ' , cost2)
                print ('cost3 FOR K3_ROBOT#1 = ' , cost4)
                time.sleep(2)
                if(cost2>cost4):
                    print ("K3_ROBOT IS COMING" )
                    j()
                if(cost4>cost2):
                    print ("K3_ROBOT IS COMING" )
                    l()                    
            if(0 in res1 and 46 in res2 and 46 in res3):
                print ("BIDDING PROCESSING AMONG K3_ROBOT#0 AND K3_ROBOT#1 " )
                time.sleep(2)
                print ('cost2 FOR K3_ROBOT = ' , cost3)
                print ('cost3 FOR K3_ROBOT#1= ' , cost4)
                time.sleep(2)
                if(cost3>cost4):
                    print ("K3_ROBOT IS COMING" )
                    m()
                if(cost4>cost3):
                    print ("K3_ROBOT IS COMING" )
                    l()                                                    
            if(0 in res1 and 0 in res2 and 46 in res3):
                print ("CHECKING PRIORITY" )
                time.sleep(2)
                print ('PRIORITY OF K3_ROBOT#1  = ' , p4)
                print ('PRIORITY OF RR  = ' , Rp)                
                time.sleep(2)
                if(Rp>p4):
                    l()                
            if(0 in res1 and 46 in res2 and 0 in res3):
                print ("CHECKING PRIORITY" )
                time.sleep(2)
                print ('PRIORITY OF K3_ROBOT#0  = ' , p2)
                print ('PRIORITY OF RR  = ' , Rp)                
                time.sleep(2)
                if(Rp>p2):
                    m()                             
            if(46 in res1 and 0 in res2 and 0 in res3):
                print ("CHECKING PRIORITY" )
                time.sleep(2)
                print ('PRIORITY OF K3_ROBOT  = ' , p)
                print ('PRIORITY OF RR  = ' , Rp)                
                time.sleep(2)
                if(Rp>p):
                    j()                        
        if ((detection3==1) or (detection4==1)):
           res=vrep.simxSetJointTargetVelocity(clientID,leftmotor1,0.00,vrep.simx_opmode_streaming) #set velocity of left motor
           res=vrep.simxSetJointTargetVelocity(clientID,rightmotor1,0.00,vrep.simx_opmode_streaming) #set velocity of right motor
        elif((detection3==1) or (detection4==1)):
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
def j ():
    vrep.simxFinish(-1) # just in case, close all opened connections
    clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP
    if clientID!=-1:
        print ('Connected to remote API server')
        vrep.simxAddStatusbarMessage(clientID,'Hello V-REP!',vrep.simx_opmode_oneshot)
        #HANDLES
        res,rightmotor=vrep.simxGetObjectHandle(clientID,'K3_rightWheelMotor#0',vrep.simx_opmode_blocking)
        res,leftmotor=vrep.simxGetObjectHandle(clientID,'K3_leftWheelMotor#0',vrep.simx_opmode_blocking)
        res,sensor1=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor1#0',vrep.simx_opmode_blocking)
        res,sensor2=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor2#0',vrep.simx_opmode_blocking)
        res,sensor3=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor3#0',vrep.simx_opmode_blocking)
        res,sensor4=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor4#0',vrep.simx_opmode_blocking)
        res,sensor5=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor5#0',vrep.simx_opmode_blocking)
        res,sensor6=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor6#0',vrep.simx_opmode_blocking)
        res,sensor7=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor7#0',vrep.simx_opmode_blocking)
        res,sensor8=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor8#0',vrep.simx_opmode_blocking)
        res,sensor9=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor9#0',vrep.simx_opmode_blocking)
        res,origin=vrep.simxGetObjectHandle(clientID,'Origin_R2',vrep.simx_opmode_blocking)
        res,wait=vrep.simxGetObjectHandle(clientID,'WaitArea',vrep.simx_opmode_blocking)
        res,goal1=vrep.simxGetObjectHandle(clientID,'Goal1',vrep.simx_opmode_blocking)
        res,goal2=vrep.simxGetObjectHandle(clientID,'Goal2',vrep.simx_opmode_blocking)
        res,goal3=vrep.simxGetObjectHandle(clientID,'Goal3',vrep.simx_opmode_blocking)
        res,object1=vrep.simxGetObjectHandle(clientID,'Object1',vrep.simx_opmode_blocking)
        res,object2=vrep.simxGetObjectHandle(clientID,'Object2',vrep.simx_opmode_blocking)
        res,object3=vrep.simxGetObjectHandle(clientID,'Object3',vrep.simx_opmode_blocking)
        res,robot=vrep.simxGetObjectHandle(clientID,'RR',vrep.simx_opmode_blocking)
        res,robot1=vrep.simxGetObjectHandle(clientID,'K3_robot',vrep.simx_opmode_blocking)    
        res,s3=vrep.simxGetObjectHandle(clientID,'K3_colorSensorRight',vrep.simx_opmode_blocking)
        #STREAMING FUNCTIONS
        res,resolution,image3=vrep.simxGetVisionSensorImage(clientID,s3,1,vrep.simx_opmode_streaming)
        res,wposition=vrep.simxGetObjectPosition(clientID,robot,-1,vrep.simx_opmode_streaming)
        res,rposition=vrep.simxGetObjectPosition(clientID,robot1,-1,vrep.simx_opmode_streaming)   
        res,eulerAngles=vrep.simxGetObjectOrientation(clientID,robot1,-1,vrep.simx_opmode_streaming)
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
        res,resolution,image3=vrep.simxGetVisionSensorImage(clientID,s3,1,vrep.simx_opmode_buffer)
        res,wposition=vrep.simxGetObjectPosition(clientID,robot,-1,vrep.simx_opmode_buffer)
        res,rposition=vrep.simxGetObjectPosition(clientID,robot1,-1,vrep.simx_opmode_buffer)
        res,eulerAngles=vrep.simxGetObjectOrientation(clientID,robot1,-1,vrep.simx_opmode_buffer)
        x2=rposition[0]
        y2=rposition[1]
        x1=wposition[0]
        y1=wposition[1]
        xw = x2-x1 #x2-x1
        yw = y2-y1 #y2-y1
        Slopeangle = math.atan2(yw,xw)*180/3.1415
        if (Slopeangle<0 and Slopeangle<-90): #correction made to ensure angle remains between 0-90
           correctionw = -1*(180 +Slopeangle)
           sp = correctionw + 1 #Range added to Slopeangle
           sm = correctionw - 1 #Range added to Slopeangle 
           rp = correctionw + 10 #Range added to continue on path
           rm = correctionw - 10 #Range added to continue on path
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

        print (Alpha)
        print (Beta)
        print (Gamma)
        if((detection3==1) or (detection4==1)):            
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
            res=vrep.simxSetJointTargetVelocity(clientID,leftmotor, -1.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res=vrep.simxSetJointTargetVelocity(clientID,rightmotor, 1.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res,detection1,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_buffer)
            res,detection2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_buffer)
            res,detection3,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor3,vrep.simx_opmode_buffer)
            res,detection4,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_buffer)
            res,detection5,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_buffer)
            res,detection6,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor6,vrep.simx_opmode_buffer)
            res,detection7,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor7,vrep.simx_opmode_buffer)
            res,detection8,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor8,vrep.simx_opmode_buffer)
            res,detection9,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor9,vrep.simx_opmode_buffer)


def m ():
    vrep.simxFinish(-1) # just in case, close all opened connections
    clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP
    if clientID!=-1:
        print ('Connected to remote API server')
        vrep.simxAddStatusbarMessage(clientID,'Hello V-REP!',vrep.simx_opmode_oneshot)
        #HANDLES
        res,rightmotor=vrep.simxGetObjectHandle(clientID,'K3_rightWheelMotor#1',vrep.simx_opmode_blocking)
        res,leftmotor=vrep.simxGetObjectHandle(clientID,'K3_leftWheelMotor#1',vrep.simx_opmode_blocking)
        res,sensor1=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor1#1',vrep.simx_opmode_blocking)
        res,sensor2=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor2#1',vrep.simx_opmode_blocking)
        res,sensor3=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor3#1',vrep.simx_opmode_blocking)
        res,sensor4=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor4#1',vrep.simx_opmode_blocking)
        res,sensor5=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor5#1',vrep.simx_opmode_blocking)
        res,sensor6=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor6#1',vrep.simx_opmode_blocking)
        res,sensor7=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor7#1',vrep.simx_opmode_blocking)
        res,sensor8=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor8#1',vrep.simx_opmode_blocking)
        res,sensor9=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor9#1',vrep.simx_opmode_blocking)
        res,origin=vrep.simxGetObjectHandle(clientID,'Origin_R2',vrep.simx_opmode_blocking)
        res,wait=vrep.simxGetObjectHandle(clientID,'WaitArea',vrep.simx_opmode_blocking)
        res,goal1=vrep.simxGetObjectHandle(clientID,'Goal1',vrep.simx_opmode_blocking)
        res,goal2=vrep.simxGetObjectHandle(clientID,'Goal2',vrep.simx_opmode_blocking)
        res,goal3=vrep.simxGetObjectHandle(clientID,'Goal3',vrep.simx_opmode_blocking)
        res,object1=vrep.simxGetObjectHandle(clientID,'Object1',vrep.simx_opmode_blocking)
        res,object2=vrep.simxGetObjectHandle(clientID,'Object2',vrep.simx_opmode_blocking)
        res,object3=vrep.simxGetObjectHandle(clientID,'Object3',vrep.simx_opmode_blocking)
        res,robot=vrep.simxGetObjectHandle(clientID,'RR',vrep.simx_opmode_blocking)
        res,robot1=vrep.simxGetObjectHandle(clientID,'K3_robot',vrep.simx_opmode_blocking)
        res,robot2=vrep.simxGetObjectHandle(clientID,'K3_robot#0',vrep.simx_opmode_blocking)
        res,s2=vrep.simxGetObjectHandle(clientID,'K3_colorSensorRight#1',vrep.simx_opmode_blocking)
        res,resolution,image2=vrep.simxGetVisionSensorImage(clientID,s2,1,vrep.simx_opmode_streaming)
        res,wposition=vrep.simxGetObjectPosition(clientID,robot,-1,vrep.simx_opmode_streaming)
        res,rposition=vrep.simxGetObjectPosition(clientID,robot2,-1,vrep.simx_opmode_streaming)   
        res,eulerAngles=vrep.simxGetObjectOrientation(clientID,robot2,-1,vrep.simx_opmode_streaming)
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
        res,resolution,image2=vrep.simxGetVisionSensorImage(clientID,s2,1,vrep.simx_opmode_buffer)
        res,wposition=vrep.simxGetObjectPosition(clientID,robot,-1,vrep.simx_opmode_buffer)
        res,rposition=vrep.simxGetObjectPosition(clientID,robot2,-1,vrep.simx_opmode_buffer)
        res,eulerAngles=vrep.simxGetObjectOrientation(clientID,robot2,-1,vrep.simx_opmode_buffer)
        x2=rposition[0]
        y2=rposition[1]
        x1=wposition[0]
        y1=wposition[1]
        xw = x2-x1 #x2-x1
        yw = y2-y1 #y2-y1
        Slopeangle = math.atan2(yw,xw)*180/3.1415
        if (Slopeangle<0 and Slopeangle<-90): #correction made to ensure angle remains between 0-90
           correctionw = -1*(180 +Slopeangle)
           sp = correctionw + 1 #Range added to Slopeangle
           sm = correctionw - 1 #Range added to Slopeangle 
           rp = correctionw + 10 #Range added to continue on path
        if (Slopeangle<0 and Slopeangle>-90): #correction made to ensure angle remains between 0-90
           correctionw = Slopeangle
           sp = correctionw + 1 #Range added to Slopeangle
           sm = correctionw - 1 #Range added to Slopeangle 
           rp = correctionw + 5 #Range added to continue on path
           rm = correctionw - 5 #Range added to continue on path   

           print('sp=',sp)
           print('rp=',rp)
           print('rm=',rm)
           print('sm=',sm)
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
        print('x2=',x2)
        print ('ALPHA=',Alpha)
        print ('BETA=',Beta)
        print ('GAMMA=',Gamma)
        if((detection3==1) or (detection4==1)):
            
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
        if ( rposition[0]>0 and  (rp<Beta and Beta>rm) and Slopeangle>-90 and Alpha<0 and Gamma<0 and ((detection1==0) and (detection2==0) and (detection3==0) and (detection4==0) and (detection5==0) and (detection6==0) or (detection3==1) and (detection5==1)  or ((detection7==1) or (detection8==1) or (detection9==1)))): #Align Khepera in 2nd and 3rd Quaderant with angle less than 90
            res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,-2.00,vrep.simx_opmode_streaming) #set velocity of left motor
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
        if ( rposition[0]>0 and  (rp>Beta and Beta>rm) and Slopeangle>-90 and Alpha<0 and Gamma<0 and ((detection1==0) and (detection2==0) and (detection3==0) and (detection4==0) and (detection5==0) and (detection6==0) or (detection3==1) and (detection5==1)  or ((detection7==1) or (detection8==1) or (detection9==1)))): #Align Khepera in 2nd and 3rd Quaderant with angle less than 90
            res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,-2.00,vrep.simx_opmode_streaming) #set velocity of left motor
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
            res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,4.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,4.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res,detection1,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_buffer)
            res,detection2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_buffer)
            res,detection3,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor3,vrep.simx_opmode_buffer)
            res,detection4,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_buffer)
            res,detection5,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_buffer)
            res,detection6,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor6,vrep.simx_opmode_buffer)
            res,detection7,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor7,vrep.simx_opmode_buffer)
            res,detection8,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor8,vrep.simx_opmode_buffer)
            res,detection9,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor9,vrep.simx_opmode_buffer)
        if (rposition[0]>0 and Beta>0 and Alpha>0 and Gamma>0 and (rp<Beta and Beta>rm) and ((detection1==0) and (detection2==0) and (detection3==0) and (detection4==0) and (detection5==0) and (detection6==0) or (detection3==1) and (detection5==1) or ((detection7==1) or (detection8==1) or (detection9==1)))): #Turning Anticlockwise in 2nd and 3rd Quaderent
            res=vrep.simxSetJointTargetVelocity(clientID,leftmotor,2.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res=vrep.simxSetJointTargetVelocity(clientID,rightmotor,-2.00,vrep.simx_opmode_streaming) #set velocity of left motor
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
            res=vrep.simxSetJointTargetVelocity(clientID,leftmotor, -1.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res=vrep.simxSetJointTargetVelocity(clientID,rightmotor, 1.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res,detection1,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_buffer)
            res,detection2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_buffer)
            res,detection3,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor3,vrep.simx_opmode_buffer)
            res,detection4,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_buffer)
            res,detection5,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_buffer)
            res,detection6,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor6,vrep.simx_opmode_buffer)
            res,detection7,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor7,vrep.simx_opmode_buffer)
            res,detection8,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor8,vrep.simx_opmode_buffer)
            res,detection9,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor9,vrep.simx_opmode_buffer)
def l ():
    vrep.simxFinish(-1) # just in case, close all opened connections
    clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP
    if clientID!=-1:
        print ('Connected to remote API server')
        vrep.simxAddStatusbarMessage(clientID,'Hello V-REP!',vrep.simx_opmode_oneshot)
        #HANDLES
        res,rightmotor=vrep.simxGetObjectHandle(clientID,'K3_rightWheelMotor#2',vrep.simx_opmode_blocking)
        res,leftmotor=vrep.simxGetObjectHandle(clientID,'K3_leftWheelMotor#2',vrep.simx_opmode_blocking)
        res,sensor1=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor1#2',vrep.simx_opmode_blocking)
        res,sensor2=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor2#2',vrep.simx_opmode_blocking)
        res,sensor3=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor3#2',vrep.simx_opmode_blocking)
        res,sensor4=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor4#2',vrep.simx_opmode_blocking)
        res,sensor5=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor5#2',vrep.simx_opmode_blocking)
        res,sensor6=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor6#2',vrep.simx_opmode_blocking)
        res,sensor7=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor7#2',vrep.simx_opmode_blocking)
        res,sensor8=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor8#2',vrep.simx_opmode_blocking)
        res,sensor9=vrep.simxGetObjectHandle(clientID,'K3_infraredSensor9#2',vrep.simx_opmode_blocking)
        res,origin=vrep.simxGetObjectHandle(clientID,'Origin_R2',vrep.simx_opmode_blocking)
        res,wait=vrep.simxGetObjectHandle(clientID,'WaitArea',vrep.simx_opmode_blocking)
        res,goal1=vrep.simxGetObjectHandle(clientID,'Goal1',vrep.simx_opmode_blocking)
        res,goal2=vrep.simxGetObjectHandle(clientID,'Goal2',vrep.simx_opmode_blocking)
        res,goal3=vrep.simxGetObjectHandle(clientID,'Goal3',vrep.simx_opmode_blocking)
        res,object1=vrep.simxGetObjectHandle(clientID,'Object1',vrep.simx_opmode_blocking)
        res,object2=vrep.simxGetObjectHandle(clientID,'Object2',vrep.simx_opmode_blocking)
        res,object3=vrep.simxGetObjectHandle(clientID,'Object3',vrep.simx_opmode_blocking)
        res,robot2=vrep.simxGetObjectHandle(clientID,'K3_robot#1',vrep.simx_opmode_blocking)
        res,robot=vrep.simxGetObjectHandle(clientID,'RR',vrep.simx_opmode_blocking)    
        res,s1=vrep.simxGetObjectHandle(clientID,'K3_colorSensorRight#2',vrep.simx_opmode_blocking)
        res,resolution,image=vrep.simxGetVisionSensorImage(clientID,s1,1,vrep.simx_opmode_streaming)
        res,wposition=vrep.simxGetObjectPosition(clientID,robot,-1,vrep.simx_opmode_streaming)
        res,rposition=vrep.simxGetObjectPosition(clientID,robot2,-1,vrep.simx_opmode_streaming)
        res,eulerAngles=vrep.simxGetObjectOrientation(clientID,robot2,-1,vrep.simx_opmode_streaming)
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
        res,wposition=vrep.simxGetObjectPosition(clientID,robot,-1,vrep.simx_opmode_buffer)
        res,rposition=vrep.simxGetObjectPosition(clientID,robot2,-1,vrep.simx_opmode_buffer)
        res,eulerAngles=vrep.simxGetObjectOrientation(clientID,robot2,-1,vrep.simx_opmode_buffer)
        x2=rposition[0]
        y2=rposition[1]
        x1=wposition[0]
        y1=wposition[1]
        xw = x2-x1 #x2-x1
        yw = y2-y1 #y2-y1
        Slopeangle = math.atan2(yw,xw)*180/3.1415
        if (Slopeangle<0 and Slopeangle<-90): #correction made to ensure angle remains between 0-90
           correctionw = -1*(180 +Slopeangle)
           sp = correctionw + 1 #Range added to Slopeangle
           sm = correctionw - 1 #Range added to Slopeangle 
           rp = correctionw + 10 #Range added to continue on path
           rm = correctionw - 10 #Range added to continue on path

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
        print (Alpha)
        print (Beta)
        print (Gamma)
        if((detection3==1) or (detection4==1)):
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
        if (Beta<0 and (sp>=Beta and Beta>=sm) and Slopeangle>-90 and Alpha<0 and Gamma<0 and rposition[0]<0 and ((detection1==0) and (detection2==0) and (detection3==0) and (detection4==0) and (detection5==0) and (detection6==0) or (detection3==1) and (detection5==1)  or ((detection7==1) or (detection8==1) or (detection9==1)))): #Align Khepera in 2nd and 3rd Quaderant with angle less than 90
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
        if (rposition[0]>0 and (sp>=Beta or Beta>=sm) and Slopeangle>-90 and Alpha>0 and Gamma>0 and  ((detection1==0) and (detection2==0) and (detection3==0) and (detection4==0) and (detection5==0) and (detection6==0) or (detection3==1) and (detection5==1)  or ((detection7==1) or (detection8==1) or (detection9==1)))): #Align Khepera in 1st and 4th Quaderant with angle less than 90
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
            res=vrep.simxSetJointTargetVelocity(clientID,leftmotor, -1.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res=vrep.simxSetJointTargetVelocity(clientID,rightmotor, 1.00,vrep.simx_opmode_streaming) #set velocity of left motor
            res,detection1,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_buffer)
            res,detection2,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_buffer)
            res,detection3,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor3,vrep.simx_opmode_buffer)
            res,detection4,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_buffer)
            res,detection5,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_buffer)
            res,detection6,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor6,vrep.simx_opmode_buffer)
            res,detection7,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor7,vrep.simx_opmode_buffer)
            res,detection8,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor8,vrep.simx_opmode_buffer)
            res,detection9,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor9,vrep.simx_opmode_buffer)

k()
j()    
m()   
l()   
