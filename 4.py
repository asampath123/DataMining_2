import numpy
import random
import math
import statistics
from numpy.core.records import record
from sklearn.cross_validation import KFold


# class TreeNode to have values and pointer for each node, the tree is built on this basic data stricture
class TreeNode:

    def __init__(self, data, label):
        self.dict = {}
        self.left = None
        self.right = None
        self.data = data
        self.label = label
        
        

#to read file and categorize values,attributes and classes.     
def extractData(fileName):
    #print("extracting file")
    file = open(fileName, 'r')
    traindata=[]
    print ("Filepath is:" + file.name)
    i=0;
    for everyLine in file:
         
        if not everyLine.strip() =='':
            if i==0:
                
                attributeTitle = everyLine.strip().split(",")
                
                #pls change the class attribute assignment based on the position of your class variable
                #refer to the cpmment post the line for changing. 
                classAttribute = attributeTitle[-1] # for data with class as the last column , iris data
                #classAttribute = attributeTitle[0] #for data with class at column 1, wine data
                
                #print(classAttribute)
                i+=1
            else:
                
                values=everyLine.strip().split(",")
                #values=list(map(float, values))
                #values = map(int, values)
                traindata.append(dict(zip(attributeTitle,values)))
            
    #print(attributeTitle)
    #print(classAttribute)
    #print(traindata)
    
    return traindata,attributeTitle,classAttribute


#highest occurance of a particular class
def frequentClassified(classValues):
    highestClass=None
    freqCount=0
    
    
    for item in classValues:
        if classValues.count(item) > freqCount:
            highestClass = item
            freqCount = classValues.count(item)
                
        
    return highestClass

#to measure information gain,we need to calcualte entropy
def entropy(subset,classAttribute):
    #print()
    frequencyList = {}
    entropyVal = 0.0

    # Calculate the frequency of each of the values in the target attr
    for item in subset:
        if (item[classAttribute] in frequencyList):
            frequencyList[item[classAttribute]] += 1.0
        else:
            frequencyList[item[classAttribute]] = 1.0
    # incomplete entropy function
    
    for freq in frequencyList.values():
        entropyVal = entropyVal + (-freq/len(subset)) * math.log(freq/len(subset), 2) 
    
    
    #print("entropy is",entropyVal)    
    return entropyVal
    


def informationGain(traindata,attributeTitle,classAttribute):
    frequencyList={}
    avgEntropy=0.0
   
    for item in traindata:
        #print(item)
        #print(attributeTitle)
        if(item[attributeTitle] in frequencyList):
            frequencyList[item[attributeTitle]] = frequencyList[item[attributeTitle]]+1.0
        else:
            frequencyList[item[attributeTitle]] = 1.0
    #print("flist is",frequencyList)        
            
    for each in frequencyList.keys():
        prob=frequencyList[each]/sum(frequencyList.values())
        subset = [item for item in traindata if item[attributeTitle] == each]
        avgEntropy=avgEntropy +prob * entropy(subset, classAttribute)
    #print("avg entropy is",avgEntropy)    
    #print("gain is",entropy(subset,classAttribute)-avgEntropy)
    #print("avgEntropy",avgEntropy)
    #print("entropy",entropy(traindata,classAttribute))
    return (entropy(traindata,classAttribute)-avgEntropy)



def calculateGini(traindata,attributeTitle,classAttribute):
    frequencyList={}
    gini=0.0
   
    for item in traindata:
        #print(item)
        #print(attributeTitle)
        if(item[attributeTitle] in frequencyList):
            frequencyList[item[attributeTitle]] = frequencyList[item[attributeTitle]]+1.0
        else:
            frequencyList[item[attributeTitle]] = 1.0
    #print("flist is",frequencyList)        
            
    for freq in frequencyList.values(): 
        gini += ((freq/len(traindata)) * (freq/len(traindata)))
    giniCoeff=1-gini
    return (giniCoeff)
    
    
            
    #print(frequencyList)        
    

# to pick the best attribute based on Gini or information gain. 
def pickBest(traindata,attributeTitle,classAttribute,flag):
    highestGain=0.0
    bestAttribute=None
    #print(attributeTitle)
    for item in attributeTitle:
        #print("attr is",item)
        
        
        if flag==1: #if Gain
            val=informationGain(traindata,item,classAttribute)
        else:     #if Gini
            val=calculateGini(traindata,item,classAttribute)
        
        
        
        if (val >= highestGain and item != classAttribute):
            
            highestGain = val
            #print("highest gain is",highestGain)
            bestAttribute = item
    
    
    #print("best is",bestAttribute)
    #print("highest gain is",highestGain)            
    return bestAttribute    


#gets data lesser than value of attr from data        
def dataLesserThanMedian(data, attr, value):
    
    data = data[:]
    dataList = []
        
    if not data:
        return dataList
    else:
        record = data.pop() #each record at a time
        
        if float(record[attr]) < value:
            #print("value of float(record[attr]) is",float(record[attr]))
            dataList.append(record) #append all values greater than median
            
            #call next set of records
            dataList.extend(dataLesserThanMedian(data, attr, value))
            return dataList
        else: 
            #call next set of records
            dataList.extend(dataLesserThanMedian(data, attr, value))
            return dataList
 
 
#gets data greater than value of attr from data        
def dataGreaterThanMedian(data, attr, value):
    
    data = data[:]
    dataList = []
        
    if not data:
        return dataList
    else:
        record = data.pop() #each record at a time
        if float(record[attr]) >= value:
            dataList.append(record) #append all values greater than median
            
            #call next set of records
            dataList.extend(dataGreaterThanMedian(data, attr, value))
            return dataList
        else:
            #call next set of records
            dataList.extend(dataGreaterThanMedian(data, attr, value))
            return dataList        



def buildTree(traindata,attributeTitle,classAttribute,flag):
    #print("buildTree")
    
    classValues=[]
    best_attr_lst = []
    list1=[]
    list2=[]
    for item in traindata:
        classValue = item[classAttribute]
        classValues.append(classValue)
    #print("frequentClassified(classValues)",frequentClassified(classValues))    
    #print(classValues)
    #print(frequentClassified(classValues))
    
    #base case 1: If trainData or attribute is empty
    if (len(attributeTitle) - 1) <= 0 or not traindata:
        freqClass = frequentClassified(classValues)
        return TreeNode(freqClass,classAttribute)
    
    #base casae 2: If all the classes of each row is same, return
    elif len(classValues)== classValues.count(classValues[0]) :
        return TreeNode(classValues[0],classAttribute) 
    
    
    
    else:
        # select the best attribute to build the tree and to select the root node
        bestAtrribute = pickBest(traindata,attributeTitle,classAttribute,flag)
        
        #pick all the values of that best attribute and find its median, we divide the data on the median
        best_attr_lst = ([record[bestAtrribute] for record in traindata])
        best_attr_lst=list(map(float, best_attr_lst))
        medianVal=statistics.median(best_attr_lst)
        #print("median is",medianVal)
        
        # get all records lesser than and greater than median of best attribute value.
        list1=dataLesserThanMedian(traindata, bestAtrribute, medianVal)
        list2=dataGreaterThanMedian(traindata, bestAtrribute, medianVal)   
        #print(list1)
        #print(list2) 
        
        #build tree to left and right using the two lists. 
        attTitle = [att for att in attributeTitle if att != bestAtrribute]
        #set data and label for the node
        root = TreeNode(medianVal, bestAtrribute)
        root.dict = traindata
        
        #insert left and right recursively 
        root.left = buildTree(list1, attTitle, classAttribute,flag)
        root.right = buildTree(list2, attTitle, classAttribute,flag)
        
    return root
 
 
# to test accuracy of the decision tree, pass test data though the tree.                    
def classifyTestData(node, record, classAttribute):
    
    
    #base case
    if node.left is None and node.right is None:
        if node.data == record[classAttribute]:
            #accurate classification
            return True
        else:
            #class not found.
            return False
    
    
    elif float(record[node.label]) > node.data:
        #traverse right subtree
        return classifyTestData(node.right, record, classAttribute)
    
    
    
    else:
        #traverse left subtree
        return classifyTestData(node.left, record, classAttribute)  
    
    
    
    
    
    
    
    
    
      

if __name__ == "__main__":
    
    
    # change name of the file you want to input 
    fileName="iris.data.txt"
    
    # to extract data, pls change the class attribute assignment based on the position of your class variable
    data,attributeTitle,classAttribute=extractData(fileName)
    
    
    #10 fold validation, set values for train data and test data based on the lenght of dataset
    folds=10
    totalLength=int(len(data)/folds)
    testLength=int(totalLength*0.1)
    trainLength=totalLength-testLength
    #print(testLength)
    #print(trainLength)
    
    #shuffle the data before training and testing
    random.shuffle(data)
    
#     kf = KFold(20, n_folds=10)
#     print(kf)
#     for train_indices, test_indices in kf:
#         print('Train: %s | test: %s' % (train_indices, test_indices))
    
    # for gini and gain
    flag=eval(input("enter 1 for gain,2 for gini  : "))
    totalAccuracy=0.0
    i=0
    while i<10:
        #print("is i",i)
        i=i+1
        traindata = data[:trainLength*i]
        testdata = data[testLength*i:]
        #print(traindata)
        #print(testdata)
        random.shuffle(data)
        
        # this method builds the decision tree
        tree=buildTree(traindata,attributeTitle,classAttribute,flag)
        
        
        accurate=0
        accuracy=0.0
        #testdata,attributeTitle,classAttribute=extractData("D://Spring 2016//DM//iris//iris3.data.txt")
        for item in testdata:
            
            if classifyTestData(tree, item, classAttribute):
                # if true, accurate classification, if not, decreases accuracy
                accurate = accurate+1
        accuracy=(accurate * 100)/len(testdata)
        
        
        print ("Accuracy in",i," fold is",round(accuracy,2))
        totalAccuracy=totalAccuracy+accuracy
    print("totalAccuracy is",totalAccuracy/folds)
    
    
    
    
    
    