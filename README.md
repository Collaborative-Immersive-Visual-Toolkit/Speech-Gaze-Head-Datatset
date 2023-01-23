# Collaborative Speech Gaze and Head Behavio Datatset

## folder structure 



## data colums

*time_seconds* : time in seconds since the start of the trial 	

*PosX PosY PosZ* : position in word coordinate of the player object 

*HeadPosX,Y,Z* : position in word coordinate of the players head 	
*HeadForward,X,Y,Z* : forward direction of the players head (i.e. direction of the nose)
*HeadUpX,Y,Z* : upward direction of the players head 

*LeftEyePosX,Y,Z* : position in word coordinate of the players left eye 
*RightEyePosX,Y,Z* : position in word coordinate of the players right eye 

*LeftEyeVecX,Y,Z* : forward direction of the players left eye 
*RightEyeVecX,Y,Z* : forward direction of the players right eye 	

*GazeX,Y,Z* : word position of the intersection between the eyes forward vector (left and right) and the data 	
*GazeU,V* : texture positon of the intersection between the eyes forward vector (left and right) and the data  (this makes it easier to underst on which element the user is whatchig) 	

*ControllerRPosX,Y,Z* : word position of the Right controller 	
*ControllerREAngX,Y,Z* : euler angles of the Right controller  	
	
*ControllerLPosX,Y,Z*: word position of the Left controller 	
*ControllerLEAngX,Y,Z* : euler angles of the Left controller  		

*PointerLeftX,Y,Z* : word position of the intersection between the Left controller direction (use euler angles to calculate) and the data
*PointerRightX,Y,Z* : word position of the intersection between the Right controller direction (use euler angles to calculate) and the data
*PointerLeftU,V* : texture positon of the intersection between the Right controller direction (use euler angles to calculate) and the data (this makes it easier to underst on which element the user is pointing at) 		
*PointerRightU,V* : texture positon of the intersection between the Left controller direction (use euler angles to calculate) and the data (this makes it easier to underst on which element the user is pointing at) 

"Condition" : 0 "undefined", 1 "CoV", 2 "CoV+Speech", 3 "eye-cursor"
"Visualization" : 0 "undefined", 1 "CoV", 2 "CoV+Speech", 3 "eye-cursor"
InsightRecording : 0 "particpant not recording"	, 1 "particpant recording"
VisualizationHalf :  	

HeadGazeX HeadGazeY HeadGazeZ	
HeadGazeU HeadGazeV
	
HeadCone00_x to HeadCone19_x
HeadCone00_y to HeadCone19_y
transcription	

## visualization data 
### textures
### elements bounding boxs 
