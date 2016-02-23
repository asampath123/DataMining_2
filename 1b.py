import numpy
import matplotlib as mpl
import matplotlib.pyplot as mplpy


def calculateMeanAndStddev(sepalLength,sepalWidth,petalLength,petalWidth):
    print("Mean of Sepal Length is",round(numpy.mean(sepalLength),2))
    print("Std_Dev of Sepal Length is",round(numpy.std(sepalLength),2))
    
    print("Mean of Sepal Width is",round(numpy.mean(sepalWidth),2))
    print("Std_Dev of Sepal Width is",round(numpy.std(sepalWidth),2))
    
    print("Mean of Petal Length is",round(numpy.mean(petalLength),2))
    print("Std_Dev of Petal Length is",round(numpy.std(petalLength),2))
    
    print("Mean of Petal Width is",round(numpy.mean(petalWidth),2))
    print("Std_Dev of Petal Width is",round(numpy.std(petalWidth),2))
    
# def plot(data,name):
#     figure = mplpy.figure(1, figsize=(9, 6))
#     axes = figure.add_subplot(111)
#     bp=axes.boxplot(data,patch_artist=True)
#     axes.set_xticklabels(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
#    ## change outline color, fill color and linewidth of the boxes
#     for box in bp['boxes']:
#         
#         # change outline color
#         box.set( color='#7570b3', linewidth=2)
#         # change fill color
#         box.set( facecolor = '#1b9e77' )
# 
#         ## change color and linewidth of the whiskers
#     for whisker in bp['whiskers']:
#         whisker.set(color='#7570b3', linewidth=2)
# 
#         ## change color and linewidth of the caps
#     for cap in bp['caps']:
#         cap.set(color='#7570b3', linewidth=2)
# 
#         ## change color and linewidth of the medians
#     for median in bp['medians']:
#         median.set(color='#b2df8a', linewidth=2)
# 
#         ## change the style of fliers and their fill
#     for flier in bp['fliers']:
#         flier.set(marker='o', color='#e7298a', alpha=0.5)
#     
#     
#     
#     
#     figure.savefig(name+'.png', bbox_inches='tight')
    
        
def extractData(fileName):
    print("extracting file")
    sepalLengthSetosa=[]
    sepalWidthSetosa=[]
    petalLengthSetosa=[]
    petalWidthSetosa=[]
    sepalLengthVersicolor=[]
    sepalWidthVersicolor=[]
    petalLengthVersicolor=[]
    petalWidthVersicolor=[]
    sepalLengthVirginica=[]
    sepalWidthVirginica=[]
    petalLengthVirginica=[]
    petalWidthVirginica=[]
    #file = open("ml-100k//u1.base", "r+")
    file = open(fileName, 'r')
    print ("Filepath is:" + file.name)
    for everyLine in file:
        if not everyLine.strip() =='':
            sepalLengths,sepalWidths,petalLengths,petalWidths,flowerClass=everyLine.strip().split(",")
            if flowerClass in "Iris-setosa":
                sepalLengthSetosa.append(float(sepalLengths))
                sepalWidthSetosa.append(float(sepalWidths))
                petalLengthSetosa.append(float(petalLengths))
                petalWidthSetosa.append(float(petalWidths))
            elif flowerClass in "Iris-versicolor":
                sepalLengthVersicolor.append(float(sepalLengths))
                sepalWidthVersicolor.append(float(sepalWidths))
                petalLengthVersicolor.append(float(petalLengths))
                petalWidthVersicolor.append(float(petalWidths))
            elif flowerClass in "Iris-virginica":
                sepalLengthVirginica.append(float(sepalLengths))
                sepalWidthVirginica.append(float(sepalWidths))
                petalLengthVirginica.append(float(petalLengths))
                petalWidthVirginica.append(float(petalWidths))
    print("------------------------------")
    print("Iris-setosa")
    calculateMeanAndStddev(sepalLengthSetosa,sepalWidthSetosa,petalLengthSetosa,petalWidthSetosa)
    print("------------------------------")
    print("Iris-versicolor")
    calculateMeanAndStddev(sepalLengthVersicolor,sepalWidthVersicolor,petalLengthVersicolor,petalWidthVersicolor)
    print("------------------------------")
    print("Iris-virginica")
    calculateMeanAndStddev(sepalLengthVirginica,sepalWidthVirginica,petalLengthVirginica,petalWidthVirginica)
    print("------------------------------")
    #calculateMeanAndStddev(sepalLengthSetosa,sepalWidthSetosa,petalLengthSetosa,petalWidthSetosa)
#     sepalLengthBox=[sepalLengthSetosa,sepalLengthVersicolor,sepalLengthVirginica]
#     sepalWidthBox=[sepalWidthSetosa,sepalWidthVersicolor,sepalWidthVirginica]
#     petalLengthBox=[petalLengthSetosa,petalLengthVersicolor,petalLengthVirginica]
#     petalWidthBox=[petalWidthSetosa,petalWidthVersicolor,petalWidthVirginica]
#     plot(sepalLengthBox,"sepalLengthBoxPlot")
#     plot(sepalWidthBox,"sepalWidthBoxPlot") 
#     plot(petalLengthBox,"petalLengthBoxPlot")
#     plot(petalWidthBox,"petalWidthBoxPlot")
extractData("D://Spring 2016//DM//iris//iris.data.txt")   