import csv
import random
import math


def main():
    trainingSet = []
    testSet = []
    split = 0.8
    filename = 'iris.data'
    loadDataset(filename,split,trainingSet,testSet)

    print(trainingSet)
    print('////')
    print(testSet)


def getNeighbours(trainingSet,testInstance,k):


'''
    Since the every value for the iris data is numeric and they all use the same units we can just use the 
    Euclidian distance betweent the two objects

    Which for objectOne = (a1,a2,...,an), objectTwo = (b1,b2,...,bn)
    distance = sqrt(Σ((ak-bk)^2))
'''
def eucDistance(objectOne,objectTwo,limit):
    distance = 0
    for i in range(limit): #Only look at the first n attribtues for each object
        attIOne = objectOne[i]
        attITwo = objectTwo[i]
        distance += (attIOne-attITwo)**2
    return math.sqrt(distance)

def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])




main()