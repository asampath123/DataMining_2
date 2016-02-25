import numpy
import math
from numpy.core.records import record



    
    
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
                classAttribute = attributeTitle[-1]
                i+=1
            else:
                values=everyLine.strip().split(",")
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
    print(attributeTitle)
    for item in attributeTitle:
        #print("attr is",item)
        gain=informationGain(traindata,item,classAttribute)
        #print(gain)
        if (gain >= highestGain and item != classAttribute):
            
            highestGain = gain
            #print("highest gain is",highestGain)
            bestAttribute = item
    
    
    print("best is",bestAttribute)
    print("highest gain is",highestGain)            
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
    unique_lst = uniqueFunction([record[attr] for record in data])
    return unique_lst
        
def get_examples(data, attr, value):
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
        if record[attr] == value:
            rtn_lst.append(record)
            rtn_lst.extend(get_examples(data, attr, value))
            return rtn_lst
        else:
            rtn_lst.extend(get_examples(data, attr, value))
            return rtn_lst    



def buildTree(traindata,attributeTitle,classAttribute):
    #print("buildTree")
    classValues=[]
    
    for item in traindata:
        classValue = item[classAttribute]
        classValues.append(classValue)
    #print(classValues)
    #print(frequentClassified(classValues))
    
    
    if (len(attributeTitle) - 1) <= 0 or not traindata:
        return frequentClassified(classValues)
    
    elif len(classValues)== classValues.count(classValues[0]) :
        return classValues[0]
    else:
        bestAtrribute = pickBest(traindata,attributeTitle,classAttribute)
        #print("build tree best",bestAtrribute)
    bestAttributeList.append(bestAtrribute) 
    print("bestAttributeList is",bestAttributeList)
    tree = {bestAtrribute:{}}
    #print(tree)    
    
    for val in get_values(traindata, bestAtrribute):
            # Create a subtree for the current value under the "best" field
            subtree = buildTree(get_examples(traindata, bestAtrribute, val),[attr for attr in attributeTitle if attr != bestAttributeList],classAttribute)
            #print(subtree)
            # Add the new subtree to the empty dictionary object in our new
            # tree/node we just created.
            tree[bestAtrribute][val] = subtree

    return tree
        
         
    #incomplete            
    #get the best attribute and build the subtree
                 
def traverseDecisionTree(item, tree):
    
    # If leaf, return
    if type(tree) == type("string"):
        return tree

    #recurse till leaf
    else:
        attribute= list(tree)[0]
        #print("classification attr is",attr)
        tempTree = tree[attribute][item[attribute]]
        #print("t is",tree)
        return traverseDecisionTree(item, tempTree)

def print_tree(tree, str):
    """
    This function recursively crawls through the d-tree and prints it out in a
    more readable format than a straight print of the Python dict object.  
    """
    if type(tree) == dict:
        print ("%s%s" % (str, list(tree)[0]))
        #for item in tree.values()[0].keys():
        for item in list(tree.values())[0]:
            print ("%s\t%s" % (str, item))
            print_tree(list(tree.values())[0][item], str + "\t")
    else:
        print ("%s\t->\t%s" % (str, tree))    
     
if __name__ == "__main__":
    
    
    traindata,attributeTitle,classAttribute=extractData("D://Spring 2016//DM//iris//iris1.data.txt")
    bestAttributeList=[]
    tree=buildTree(traindata,attributeTitle,classAttribute)
    
    
    
    
    
    
    testdata,attributeTitle,classAttribute=extractData("D://Spring 2016//DM//iris//iris3.data.txt")
    testclassification=[]
    #for item in testdata:
    #    testclassification.append(traverseDecisionTree(item, tree))
    #classification = classify(tree, data)
    #for item in testclassification:
    #    print(item)
    #print(tree)  
    #print_tree(tree,"")    
    
    
    
    
    
        
    
    