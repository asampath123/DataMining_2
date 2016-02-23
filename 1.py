import numpy


def calculateMeanAndStddev(sepalLength,sepalWidth,petalLength,petalWidth):
    print("Mean of Sepal Length is",round(numpy.mean(sepalLength),2))
    print("Std_Dev of Sepal Length is",round(numpy.std(sepalLength),2))
    
    print("Mean of Sepal Width is",round(numpy.mean(sepalWidth),2))
    print("Std_Dev of Sepal Width is",round(numpy.std(sepalWidth),2))
    
    print("Mean of Petal Length is",round(numpy.mean(petalLength),2))
    print("Std_Dev of Petal Length is",round(numpy.std(petalLength),2))
    
    print("Mean of Petal Width is",round(numpy.mean(petalWidth),2))
    print("Std_Dev of Petal Width is",round(numpy.std(petalWidth),2))
    
    
def extractData(fileName):
    print("extracting file")
    FlowerDict =[]
    sepalLength=[]
    sepalWidth=[]
    petalLength=[]
    petalWidth=[]
    #file = open("ml-100k//u1.base", "r+")
    file = open(fileName, 'r')
    print ("Filepath is:" + file.name)
    for everyLine in file:
        if not everyLine.strip() =='':
            sepalLengths,sepalWidths,petalLengths,petalWidths,flowerClass=everyLine.strip().split(",")
            #FlowerDict.append(sepalLength,sepalWidth,petalLength,petalWidth,flowerClass)
            sepalLength.append(float(sepalLengths))
            sepalWidth.append(float(sepalWidths))
            petalLength.append(float(petalLengths))
            petalWidth.append(float(petalWidths))
    calculateMeanAndStddev(sepalLength,sepalWidth,petalLength,petalWidth)
     

extractData("D://Spring 2016//DM//iris//iris.data.txt")   