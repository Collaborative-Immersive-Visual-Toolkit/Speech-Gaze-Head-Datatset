# Collaborative Speech Gaze and Head Behavio Datatset

## Folder structure 

The dataset contains 2 folders: ***Data***, ***Visualizations***

The ***Data*** folders contains 10 foilders each representing one of the ***experimental session***.<br />
Each ***experimental session*** folder is named with the ***dayNumber_hourNumber*** ( 365 days a hear 24 hours a day).<br />
Each ***experimental session*** contains 3 ***experimental trials*** folder, each folder name is composed by the ***experimentalCondition_visualizationNumber***<br />
The ***experimenta lConditions*** are 1 = "CoV", 2 = "CoV+Speech", 3 = "eye-cursor".<br />
The ***visualization Number*** are 1 = "Movie Dataset", 2 = "Gender bias in Movie Dataset", 3 = "Car insurance risk Dataset".<br />
Within each ***experimental trials*** there is a ***data.csv*** file, the section Columns describe the data contained with the CSV file. 

## Colums

Each  ***data.csv*** file contains the 218 columns.  <br />
A part from ***time_seconds*** all other colums have a either ***U1*** ***U2*** prefix indicating the user. <br />
For example ***LeftEyePosX,Y,Z*** means there will be 6 different columns: ***U1LeftEyePosX, U1LeftEyePosY, U1LeftEyePosZ, U2LeftEyePosX, U2LeftEyePosY, U2LeftEyePosZ***

<sub>
time_seconds : time in seconds since the start of the trial 	<br />
PosX,Y,Z : position in word coordinate of the player object <br />
HeadPosX,Y,Z : position in word coordinate of the players head<br /> 	
HeadForward,X,Y,Z : forward direction of the players head (i.e. direction of the nose)<br />
HeadUpX,Y,Z : upward direction of the players head <br />
LeftEyePosX,Y,Z : position in word coordinate of the players left eye <br />
RightEyePosX,Y,Z : position in word coordinate of the players right eye <br />
LeftEyeVecX,Y,Z : forward direction of the players left eye <br />
RightEyeVecX,Y,Z : forward direction of the players right eye <br />	
GazeX,Y,Z : word position of the intersection between the eyes forward vector (left and right) and the data 	<br />
GazeU,V : texture positon of the intersection between the eyes forward vector (left and right) and the data  (this makes it easier to underst on which element the user is whatchig) 	<br />
ControllerRPosX,Y,Z : word position of the Right controller <br />	
ControllerREAngX,Y,Z : euler angles of the Right controller  <br />	
ControllerLPosX,Y,Z : word position of the Left controller <br />	
ControllerLEAngX,Y,Z : euler angles of the Left controller <br /> 		
PointerLeftX,Y,Z : word position of the intersection between the Left controller direction (use euler angles to calculate) and the data <br />
PointerRightX,Y,Z : word position of the intersection between the Right controller direction (use euler angles to calculate) and the data <br />
PointerLeftU,V : texture positon of the intersection between the Right controller direction and the data (this makes it easier to underst on which element the user is pointing at) 	<br />	
PointerRightU,V : texture positon of the intersection between the Left controller direction and the data (this makes it easier to underst on which element the user is pointing at) <br />
Condition : integer value indicating the experimental condition  ( 0 "undefined", 1 "CoV", 2 "CoV+Speech", 3 "eye-cursor" ) <br />
Visualization : integer value indicating the dataset  ( 0 "undefined", 1 "Movie Dataset", 2 "Gender bias in Movie Dataset", 3 "Car insurance risk Dataset" )<br />
InsightRecording : binary valu indicating if the user is recording an insight or not  ( 0 "particpant not recording" , 1 "particpant recording" )<br />
VisualizationHalf :  integer value indicating which half of the visualization is beeing displayed ( 0 "first" , 1 "second" )	<br />
HeadGazeX,Y,Z : word position of the intersection between the head forward vector and the data<br /> 	 	
HeadGazeU,V : texture positon of the intersection between the head forward vector and the data  (this makes it easier to underst on which element the user head is pointing at) 	<br />
HeadCone00_x to HeadCone19_x : U coordinate position of the 20 points of the projected CoV (for the CoV + Speech such coordinate are dynamic)<br />
HeadCone00_y to HeadCone19_y : V coordinate position of the 20 points of the projected CoV (for the CoV + Speech such coordinate are dynamic)<br />
transcription : this is the data extracted from the audio files with the whisper model (audio files not included due to anonimoization)	<br />
</sub>

## Visualizations 

The visualization section contains information about the segmented environment 

### Textures

### Elements bounding boxs 
