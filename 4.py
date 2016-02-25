import numpy
import random
import math
import statistics
from numpy.core.records import record

class Node:

    def __init__(self, value, value1):
        self.left = None
        self.data = value
        self.label = value1
        self.right = None
        self.dict = {}

    
def extractData(fileName):
    print("extracting file")
    file = open(fileName, 'r')
    traindata=[]
    print ("Filepath is:" + file.name)
    i=0;
    for everyLine in file:
         
        if not everyLine.strip() =='':
            if i==0:
                attributeTitle = everyLine.strip().split(",")
                classAttribute = attributeTitle[-1] # for data with class as the last column
                #classAttribute = attributeTitle[0] #for data with class at column 1, wine data
                print(classAttribute)
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



def frequentClassified(classValues):
    highestClass=None
    freqCount=0
    
    
    for item in classValues:
        if classValues.count(item) > freqCount:
            highestClass = item
            freqCount = classValues.count(item)
            
            
    return highestClass        

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
    
    
            
    #print(frequencyList)        
    

def pickBest(traindata,attributeTitle,classAttribute):
    highestGain=0.0
    bestAttribute=None
    #print(attributeTitle)
    for item in attributeTitle:
        #print("attr is",item)
        gain=informationGain(traindata,item,classAttribute)
        #print(gain)
        if (gain >= highestGain and item != classAttribute):
            
            highestGain = gain
            #print("highest gain is",highestGain)
            bestAttribute = item
    
    
    #print("best is",bestAttribute)
    #print("highest gain is",highestGain)            
    return bestAttribute    

def uniqueFunction(lst):
    """
    Returns a list made up of the unique values found in lst.  i.e., it
    removes the redundant values in lst.
    """
    lst = lst[:]
    unique_lst = []

    # Cycle through the list and add each value to the unique list only once.
    for item in lst:
        if unique_lst.count(item) <= 0:
            unique_lst.append(item)
            
    # Return the list with all redundant values removed.
    return unique_lst


def get_values(data, attr):
    """
    Creates a list of values in the chosen attribut for each record in data,
    prunes out all of the redundant values, and return the list.  
    """
    data = data[:]
    #print("get values function")
    #print(attr)
    #for record1 in data:
        #print(record1)
#     print([record[attr] for record in data])
    unique_lst = ([record[attr] for record in data])
    unique_lst=list(map(float, unique_lst))
    return unique_lst
        
def get_lesser(data, attr, value):
    """
    Returns a list of all the records in <data> with the value of <attr>
    matching the given value.
    """
    data = data[:]
    rtn_lst = []
        
    if not data:
        return rtn_lst
    else:
        record = data.pop()
        #print("record is",record)
        if float(record[attr]) < value:
            #print("value of float(record[attr]) is",float(record[attr]))
            rtn_lst.append(record)
            rtn_lst.extend(get_lesser(data, attr, value))
            return rtn_lst
        else:
            rtn_lst.extend(get_lesser(data, attr, value))
            return rtn_lst
        
def get_greater(data, attr, value):
    """
    Returns a list of all the records in <data> with the value of <attr>
    matching the given value.
    """
    data = data[:]
    rtn_lst = []
        
    if not data:
        return rtn_lst
    else:
        record = data.pop()
        if float(record[attr]) >= value:
            rtn_lst.append(record)
            rtn_lst.extend(get_greater(data, attr, value))
            return rtn_lst
        else:
            rtn_lst.extend(get_greater(data, attr, value))
            return rtn_lst        



def buildTree(traindata,attributeTitle,classAttribute):
    #print("buildTree")
    classValues=[]
    unique_lst = []
    list1=[]
    list2=[]
    for item in traindata:
        classValue = item[classAttribute]
        classValues.append(classValue)
    #print("frequentClassified(classValues)",frequentClassified(classValues))    
    #print(classValues)
    #print(frequentClassified(classValues))
    
    
    if (len(attributeTitle) - 1) <= 0 or not traindata:
        freqClass = frequentClassified(classValues)
        return Node(freqClass,classAttribute)
    
    elif len(classValues)== classValues.count(classValues[0]) :
        return Node(classValues[0],classAttribute) 
    else:
        bestAtrribute = pickBest(traindata,attributeTitle,classAttribute)
        
        unique_lst = ([record[bestAtrribute] for record in traindata])
        #print(unique_lst)
        unique_lst=list(map(float, unique_lst))
        #print(unique_lst)
        medianVal=statistics.median(unique_lst)
        #print("median is",medianVal)
        
    
        list1=get_lesser(traindata, bestAtrribute, medianVal)
        list2=get_greater(traindata, bestAtrribute, medianVal)   
        #print(list1)
        #print(list2) 
        
        k = [a for a in attributeTitle if a != bestAtrribute]
        root = Node(medianVal, bestAtrribute)
        root.dict = traindata
        root.left = buildTree(list1, k, classAttribute)
        root.right = buildTree(list2, k, classAttribute)
        
    return root
    #print("done")
    #return tree
        
         
    #incomplete            
    #get the best attribute and build the subtree
                 

    
def classifyTestData(node, record, classAttribute):
    if node.left is None and node.right is None:
        if node.data == record[classAttribute]:
            return True
        else:
            return False
    elif float(record[node.label]) > node.data:
        return classifyTestData(node.right, record, classAttribute)
    else:
        return classifyTestData(node.left, record, classAttribute)    

if __name__ == "__main__":
    
    
    data,attributeTitle,classAttribute=extractData("D://Spring 2016//DM//iris//iris1.data.txt")
    bestAttributeList=[]
    random.shuffle(data)

    totalAccuracy=0.0
    i=0
    while i<10:
        print("is i",i)
        i=i+1
        traindata = data[:11*i]
        testdata = data[3*i:]
        #print(traindata)
        #print(testdata)
        
        
        tree=buildTree(traindata,attributeTitle,classAttribute)
        
       
        accurate=0
        accuracy=0.0
        #testdata,attributeTitle,classAttribute=extractData("D://Spring 2016//DM//iris//iris3.data.txt")
        for item in testdata:
            if classifyTestData(tree, item, classAttribute):
                accurate = accurate+1
        accuracy=(accurate * 100)/len(testdata)       
        print ("Accuracy for the decision tree is", round(accuracy,2))
        totalAccuracy=totalAccuracy+accuracy
    print("totalAccuracy is",totalAccuracy/10)   
            
        
    
    
    
    
        
    
    