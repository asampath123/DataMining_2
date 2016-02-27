import scipy
from scipy.stats.stats import pearsonr
import numpy
import matplotlib.pyplot

def getMax(wineMatrix):
    
    maxarray=[0,0,0,0,0,0,0,0]
    for subarray in wineMatrix:
        for sub in subarray:
            if sub>min(maxarray) and sub!=1.0:
                maxarray.remove(min(maxarray))
                maxarray.append(sub)
    maxarray=numpy.unique(maxarray)
    print("max co-efficients are",maxarray)
    for i in range(0,4):                    
        a=[(index, row.index(maxarray[i])) for index, row in enumerate(wineMatrix) if maxarray[i] in row]            
        print("their indexes",end="")
        print(a)

def getMin(wineMatrix):
    
    minarray=[1,1,1,1,1,1,1,1]
    
    for subarray in wineMatrix:
        for sub in subarray:
            
            if sub<max(minarray) and sub>0.0:
                minarray.remove(max(minarray))
                minarray.append(sub)
    minarray=numpy.unique(minarray)
    print("minimum 4 co-efficients are",minarray)
    for i in range(0,4):                    
        a=[(index, row.index(minarray[i])) for index, row in enumerate(wineMatrix) if minarray[i] in row]            
        print("their indexes",end="")
        print(a)        
        
    


def extractData(fileName):
    print("extracting file")
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    list6=[]
    list7=[]
    list8=[]
    list9=[]
    list10=[]
    list11=[]
    list12=[]
    list13=[]
    list14=[]
    
    #file = open("ml-100k//u1.base", "r+")
    file = open(fileName, 'r')
    print ("Filepath is:" + file.name)
    for everyLine in file:
        if not everyLine.strip() =='':
            classval,alcohol,malicAcid,ash,alcanalityOfAsh,magnesium,totalPhenol,flavanoid,nanFlavanoidPhenol,proanthocyanin,colorIntensity,hue,OD_dilutedWine,proline=everyLine.strip().split(",")
            #FlowerDict.append(sepalLength,sepalWidth,petalLength,petalWidth,flowerClass)
            list1.append(float(classval))
            list2.append(float(alcohol))
            list3.append(float(malicAcid))
            list4.append(float(ash))
            list5.append(float(alcanalityOfAsh))
            list6.append(float(magnesium))
            list7.append(float(totalPhenol))
            list8.append(float(flavanoid))
            list9.append(float(nanFlavanoidPhenol))
            list10.append(float(proanthocyanin))
            list11.append(float(colorIntensity))
            list12.append(float(hue))
            list13.append(float(OD_dilutedWine))
            list14.append(proline)
    
    
    #print(a)
    row=14
    column=14
    wineMatrix=[[0 for i in range(row)]for j in range(column)]
    a1=[]
    for i in range(1,14):
        x=eval("list"+str(i))
        xInStr="list"+str(i)
        #print("list is",x)
        for j in range(1,14):
            y=eval("list"+str(j))
            yInstr="list"+str(j)
            #print("list2 is",y)
            a1,p=pearsonr(x, y)
            #print("co-eff of",xInStr,end="")
            #print("and",yInstr,end="")
            #print("is",a1)
            wineMatrix[i][j]=a1  
            #print(wineMatrix)
    
    
    getMax(wineMatrix)
    getMin(wineMatrix)
    
#     maximum output
#     their indexes[(8, 10), (10, 8)]
#     their indexes[(7, 13), (13, 7)]
#     their indexes[(8, 13), (13, 8)]
#     their indexes[(7, 8), (8, 7)]
    matplotlib.pyplot.scatter(list8, list10,color='r', marker='s', alpha=.4)
    matplotlib.pyplot.show()
    matplotlib.pyplot.scatter(list7, list13,color='b', marker='s', alpha=.4)
    matplotlib.pyplot.show()     
    matplotlib.pyplot.scatter(list8, list13,color='g', marker='s', alpha=.4)
    matplotlib.pyplot.show()
    matplotlib.pyplot.scatter(list7, list8,color='c', marker='s', alpha=.4)
    matplotlib.pyplot.show()
    
#     minimum output
#     their indexes[(4, 13), (13, 4)]
#     their indexes[(4, 10), (10, 4)]
#     their indexes[(5, 11), (11, 5)]
#     their indexes[(6, 12), (12, 6)]

    matplotlib.pyplot.scatter(list4, list13,color='r', marker='s', alpha=.4)
    matplotlib.pyplot.show()
    matplotlib.pyplot.scatter(list4, list10,color='b', marker='s', alpha=.4)
    matplotlib.pyplot.show()     
    matplotlib.pyplot.scatter(list5, list11,color='g', marker='s', alpha=.4)
    matplotlib.pyplot.show()
    matplotlib.pyplot.scatter(list6, list12,color='c', marker='s', alpha=.4)
    matplotlib.pyplot.show()
    

             
extractData("wine1.data.txt") 