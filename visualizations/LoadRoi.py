from tkinter.tix import ButtonBox
from turtle import width
import pandas as pd
from shapely.geometry import Point, Polygon 
from shapely import affinity

class visualization:

    def __init__(self, visNumber, vistype):
        
        self.number_of_screens = 8
        self.single_screen_width = 980
        self.width=self.single_screen_width*self.number_of_screens #width perscreen number
        self.heigth=551

        self.visualizationOrder = [
            "BoxAndWhiskers",
            "BoxAndWhiskers2",
            "Scatterplot2",
            "Scatterplot1",
            "Oscar",
            "Instructions",
            "StackBarChart",
            "Histograms"]

        self.v1 = [ item +".png" for item in self.visualizationOrder] 
        self.v2 = [ item +"_Gender.png" for item in self.visualizationOrder] 
        self.v3 = [ item +"_Third.png" for item in self.visualizationOrder] 

        self.bbox=pd.DataFrame(columns=["","",])

        self.img_csv = "TexturesNew/out_ROI.csv" if vistype=='Graph' else "TexturesNew/out_ROI_page.csv"

        self.polys = []

        self.visNumber = visNumber

        self.polysShifted = self.polys

        self.LoadVis()

    def LoadVis(self):

        df = pd.read_csv(self.img_csv)

        df['image'] = [ item.replace("TexturesNew\\","") for item in df['image'].to_list() ]

        if(self.visNumber==1): V = self.v1
        elif(self.visNumber==2): V = self.v2
        elif(self.visNumber==3): V = self.v3
        
        df = df.loc[(df['image'] == V[0]) | (df['image'] == V[1]) | (df['image'] == V[2]) | (df['image'] == V[3]) | 
        (df['image'] == V[4]) | (df['image'] == V[5]) | (df['image'] == V[6]) | (df['image'] == V[7])]

        self.bbox=pd.DataFrame(columns=df.columns)

        for index,screen in enumerate(V):
            newbbox = df.loc[(df['image'] == screen)]
            newbbox['x1'] = 980-newbbox['x1']+(self.single_screen_width*index)
            newbbox['x2'] = 980-newbbox['x2']+(self.single_screen_width*index)
            self.bbox = self.bbox.append(newbbox)

        for row in self.bbox.iterrows():
            coords = [(row[1]['x1'], row[1]['y1']), (row[1]['x2'], row[1]['y1']), (row[1]['x2'], row[1]['y2']), (row[1]['x1'], row[1]['y2'])]
            self.polys.append(Polygon(coords))

    def AOI(self,u,v):
        
        roilist =[]

        p1 = Point(u, v)

        for index,poly in enumerate(self.polys):
            if p1.within(poly):
                roilist.append(index)
        
        return roilist
    

if __name__ == "__main__":
    
    Vis = visualization(1)
    a = Vis.AOI(700,150)
    print(a)