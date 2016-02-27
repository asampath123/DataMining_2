import pandas
from scipy.spatial import distance
import numpy
from scipy.spatial.distance import pdist
from sklearn import preprocessing

def euclieanDist(data):
    
    
    classDistList = {}
    
    #calcualte the euclidean distance
    distanceMatrix=distance.squareform(pdist(data,'euclidean'))
    
    
    filler=numpy.inf
    print(filler)
    numpy.fill_diagonal(distanceMatrix, filler)
    
    
    #calculate nearest elements of the matrix 
    minimumDistInMatrix=distanceMatrix.argmin(axis=0)
    
    
   
    for i,j in enumerate(minimumDistInMatrix):
        class1 = data[0].iloc[i]
        class2 = data[0].iloc[j]
        
        classAtt=classDistList.get(class1)
        if not classAtt:
            classDistList[class1]=[0,0]

        if class1 == class2:
            classDistList[class1][0]=classDistList[class1][0]+1
        classDistList[class1][1] = classDistList[class1][1] + 1
    
    classCount=0
    totalCount = 0
    total=0
    for a,b in classDistList.items():
        print("In class",a,", the % of points whose close neighbors belong to same class",(b[0]/b[1])*100)
        classCount = classCount + b[0]
        totalCount = totalCount + b[1]
        total=(classCount/totalCount)*100
    print()
    print("at datalevel",total)
   
    
    

def normalize(data,flag):
    if flag==1:
        return pandas.DataFrame(preprocessing.scale(data))
    else:
        return pandas.DataFrame(preprocessing.MinMaxScaler().fit_transform(data))
        
    print()

data = pandas.read_csv('wine.csv', sep=',',header = None)
#print(data)
wihoutClassData=data.drop(data.columns[0], axis=1)
#print(wihoutClassData)
#print(data)

euclieanDist(data)
#1 for z-score,0 for 0-1 normalization 
flag=1
normalizedData=normalize(wihoutClassData,flag)
#print(normalizedData)
data[data.columns[[1,2,3,4,5,6,7,8,9,10,11,12,13]]] = normalizedData[normalizedData.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12]]]
#print(data)
euclieanDist(data)