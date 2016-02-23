import scipy
from scipy.stats.stats import pearsonr

def extractData(fileName):
    print("extracting file")
    alcohols =[]
    malicAcids=[]
    ashs=[]
    alcanalityOfAshs=[]
    magnesiums=[]
    totalPhenols=[]
    flavanoids =[]
    nanFlavanoidPhenols=[]
    proanthocyanins=[]
    colorIntensities=[]
    hues=[]
    OD_dilutedWines=[]
    prolines=[]
    #file = open("ml-100k//u1.base", "r+")
    file = open(fileName, 'r')
    print ("Filepath is:" + file.name)
    for everyLine in file:
        if not everyLine.strip() =='':
            alcohol,malicAcid,ash,alcanalityOfAsh,magnesium,totalPhenol,flavanoid,nanFlavanoidPhenol,proanthocyanin,colorIntensity,hue,OD_dilutedWine,proline,extra=everyLine.strip().split(",")
            #FlowerDict.append(sepalLength,sepalWidth,petalLength,petalWidth,flowerClass)
            alcohols.append(int(alcohol))
            malicAcids.append(float(malicAcid))
            ashs.append(float(ash))
            alcanalityOfAshs.append(float(alcanalityOfAsh))
            magnesiums.append(float(magnesium))
            totalPhenols.append(int(totalPhenol))
            flavanoids.append(float(flavanoid))
            nanFlavanoidPhenols.append(float(nanFlavanoidPhenol))
            proanthocyanins.append(float(proanthocyanin))
            colorIntensities.append(float(colorIntensity))
            hues.append(float(hue))
            OD_dilutedWines.append(float(OD_dilutedWine))
            prolines.append(proline)
            
    a1=pearsonr(alcohols, malicAcids)
    print(a1)       
            
    #calculateMeanAndStddev(sepalLength,sepalWidth,petalLength,petalWidth)
     
   
extractData("D://Spring 2016//DM//iris//wine.data.txt") 