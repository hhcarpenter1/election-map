from	graphics	import	*
win = GraphWin("Map", 1000, 1000)
countyNames = []
import re
p = re.compile(r'[A-Z]')
noNumbers = re.compile(r'[^0-9]')
###Gets the coordinates of each county
with open('IL.txt') as f:
   dataList = []
###Gets the county names
   for line in f:
      fields = line.split()
      word = ''.join(fields)
      ##Eliminates strings that are not counties
      if (word != "IL" and fields != [] and re.match(noNumbers, line)): 
         dataList.append(fields)
   i = 0
   ##Adds counties to a list
   while i < len(dataList):
         m = p.search(str(dataList[i])) 
         if m:    
            county = dataList[i] 
            countyNames.append(county)
         i+=1
   coordinates = []
   j = 0
   countyList = []
   myDict = {}
   myDict['coodinates'] = []
   myDict['county'] = str
   ##Matches each county with its coordinates
   for d in dataList:
      if (j != len(countyNames)):
         string = ''.join(d)
         county = ''.join(countyNames[j])
      if (string != county):
         coordinates.append(d)  
      if (string == county and j!= len(countyNames)):
         myDict['coordinates'] = coordinates
         myDict['county'] = county
         countyList.append(myDict)
         myDict = {}
         coordinates = []
         j+=1
i = len(dataList)-1
##while loop to get the coordinates of the last item of the list
while (dataList[i] != countyNames[len(countyNames)-1]):
   points = dataList[i]
   coordinates.append(points) 
   if (dataList[i-1] == countyNames[len(countyNames)-1]):
         myDict['coordinates'] = coordinates
         myDict['county'] = countyNames[len(countyNames)-1]
         countyList.append(myDict)
   i-=1
Points = []
myList = []
currCounty = []
count = 0
colorDict = {}
colorList = []
###Receives voter data
with open('IL2012.txt') as f:  
   count = 0   
   ###Matches votor data for each county with a color
   for line in f: 
         fields = line.split()
         word = re.sub(r'\,', " ", line)
         word = word.split()
         if (count > 0):
            word3 = ''.join(word[3])
            word1 = ''.join(word[1])
            word2 = ''.join(word[2])        
            colorDict['Other'] = word3
            colorDict['Red'] = word1
            colorDict['Blue'] = word2
         colorList.append(colorDict)
         colorDict = {}
         count+=1
   AllShades = []
   countyShade = color_rgb(0, 0, 0)
   ###Adds voter data for each county into a list    
   for d in colorList:
      values = d.values()
      if (len(values) != 0):
         r = values[0]
         g = values[1]
         b = values[2]
         CountyShade = [r,g,b]
         AllShades.append(CountyShade)
myCount = 0
###The part of the code that focuses on the shade colors and drawing the counties
for c in countyList: 
    myList = c['coordinates']
    for i in myList:
         x = (float(i[0])*100)+9300 ##*100)+9300 adjusts position of x cord
         y = (-float(i[1])*100)+4300 ##*100)+4300 adjusts position of y cord
         Points.append(Point(x,y))         
    p = Polygon(Points)
    voterPop = AllShades[myCount-1]
    b = int(voterPop[0])
    g = int(voterPop[1])
    r = int(voterPop[2])
    pop = r + g + b
    BlueShade = (255 * b)/pop
    RedShade = (255 * r)/pop
    GreenShade = (255 * g)/pop
    p.setFill(color_rgb(RedShade, GreenShade, BlueShade))  
    p.draw(win)
    count+=1
    ##To make sure myCounty doesn't create an out of bounds exception  
    if (myCount != len(AllShades)-1):
       myCount+=1
    Points = []
win.getMouse()
win.close()
    
    













