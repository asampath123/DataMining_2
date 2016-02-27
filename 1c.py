import numpy
import matplotlib as mpl
import matplotlib.pyplot as mplpy



    
def plot(data,name):
    
    
    figure = mplpy.figure(1, figsize=(9, 6))
    axes = figure.add_subplot(111)
    boxplots=axes.boxplot(data,patch_artist=True)
    axes.set_xticklabels(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
## change outline color, fill color and linewidth of the boxes
    for box in boxplots['boxes']:
        
       
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#1b9e77' )

        
    for whisker in boxplots['whiskers']:
        whisker.set(color='#7570b3', linewidth=2)

        
    for cap in boxplots['caps']:
        cap.set(color='#7570b3', linewidth=2)

        
    for median in boxplots['medians']:
        median.set(color='#b2df8a', linewidth=2)

        
    for flier in boxplots['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)
    
    
    
    
    figure.savefig(name+'.png', bbox_inches='tight')
    
        
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
#     
    sepalLengthBox=[sepalLengthSetosa,sepalLengthVersicolor,sepalLengthVirginica]
    sepalWidthBox=[sepalWidthSetosa,sepalWidthVersicolor,sepalWidthVirginica]
    petalLengthBox=[petalLengthSetosa,petalLengthVersicolor,petalLengthVirginica]
    petalWidthBox=[petalWidthSetosa,petalWidthVersicolor,petalWidthVirginica]
    #plot(sepalLengthBox,"sepalLengthBoxPlot")
    #plot(sepalWidthBox,"sepalWidthBoxPlot") 
    #plot(petalLengthBox,"petalLengthBoxPlot")
    plot(petalWidthBox,"petalWidthBoxPlot")
    print(max(petalLengthVirginica))
    print("Done plotting,check your folder for images of box plot")
extractData("D://Spring 2016//DM//iris//iris.data.txt")   