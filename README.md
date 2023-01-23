# Collaborative Speech Gaze and Head Behavio Datatset

## Folder structure 

The dataset contains 2 folders: ***Data***, ***Visualizations***

The ***Data*** folders contains 10 foilders each representing one of the ***experimental session***.<br />
Each ***experimental session*** folder is named with the ***dayNumber_hourNumber*** ( 365 days a hear 24 hours a day).<br />
Each ***experimental session*** contains 3 ***experimental trials*** folder, each folder name is composed by the ***experimentalCondition_visualizationNumber***<br />
The ***experimenta lConditions*** are 1 = "CoV", 2 = "CoV+Speech", 3 = "eye-cursor".<br />
The ***visualization Number*** are 1 = "Movie Dataset", 2 = "Gender bias in Movie Dataset", 3 = "Car insurance risk Dataset".<br />

## Colums

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

*Condition* : integer value indicating the experimental condition  ( 0 "undefined", 1 "CoV", 2 "CoV+Speech", 3 "eye-cursor" ) 
*Visualization* : integer value indicating the dataset  ( 0 "undefined", 1 "Movie Dataset", 2 "Gender bias in Movie Dataset", 3 "Car insurance risk Dataset" )
*InsightRecording* : binary valu indicating if the user is recording an insight or not  ( 0 "particpant not recording" , 1 "particpant recording" )
*VisualizationHalf* :  integer value indicating which half of the visualization is beeing displayed ( 0 "first" , 1 "second" )	

*HeadGazeX,Y,Z* : word position of the intersection between the head forward vector and the data 	 	
*HeadGazeU,V* : texture positon of the intersection between the head forward vector and the data  (this makes it easier to underst on which element the user head is pointing at) 	
	
HeadCone00_x to HeadCone19_x : U coordinate position of the 20 points of the projected CoV (for the CoV + Speech such coordinate are dynamic)
HeadCone00_y to HeadCone19_y : V coordinate position of the 20 points of the projected CoV (for the CoV + Speech such coordinate are dynamic)
transcription : this is the data extracted from the audio files with the whisper model (audio files not included due to anonimoization)	

## Visualizations 

The visualization section contains information about the segmented environment 

### Textures

### Elements bounding boxs 
