import csv
import random
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



def main():
    trainingSet = []
    testSet = []
    split = 0.8
    filename = 'iris.data'
    loadDataset(filename,split,trainingSet,testSet)
    predictions = []
    k = 4
    for obj in testSet:
        neighbours = getNeighbours(trainingSet,obj,k)
        objClass = classify(neighbours)
        predictions.append({'data': obj, 'prediction': objClass, 'correct': objClass == obj[-1]})
    colourCodes = {'Iris-setosa': '#ca5b78', 'Iris-versicolor': '#3f9e66', 'Iris-virginica':'#059dc5','Iris-setosaCor': '#f89675', 'Iris-versicolorCor': '#73e1a7','Iris-virginicaCor':'#64d4fd','Iris-setosaWro': '#742319', 'Iris-versicolorWro': '#22501d','Iris-virginicaWro':'#224060' }
    plotSet(trainingSet,colourCodes,predictions)

def plotSet(data,colourCodes, predictions=None):
    xs = []
    ys = []
    zs = []
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for obj in data:
        xs = obj[0]
        ys = obj[1]
        zs = obj[2]
        col = colourCodes[obj[-1]]
        ax.scatter(xs, ys, zs, c=col,marker='o')

    for obj in predictions:
        xs = obj['data'][0]
        ys = obj['data'][1]
        zs = obj['data'][2]
        col = obj['data'][-1]
        if obj['correct']:
            col +='Cor'
        else:
            col+='Wro'
        col = colourCodes[col]
        ax.scatter(xs, ys, zs, c=col,marker='o')

        
    ax.set_xlabel('Sepal Length (cm)')
    ax.set_ylabel('Sepal Width (cm)')
    ax.set_zlabel('Petal Length (cm)')
    plt.show()


'''
    Raw Accuracy, what % did we predict right
'''
def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0

'''
    This is where we count up the number of class A's vs class B's and return has the majority
    Possible options, weight by distance.
    Approach:
        Create a dictionary {aCount: 0, bCount: 0}
        for each neighbour look at its class, if a => aCount +=1 otherwise bCount +=1
        return the class that's the largest
'''
def classify(neighbours):
    countHash = {}
    for neighbour in neighbours:
        nClass = neighbour[0][-1]
        if nClass in countHash:
            countHash[nClass] += 1
        else:
            countHash[nClass] = 1
    sorted_by_value = sorted(countHash.items(), key=lambda kv: kv[1])
    return sorted_by_value[0][0]


'''
    Approach: Find all distances between our testInstance and our trainingset, sort it, take the k closest
'''
def getNeighbours(trainingSet,testInstance,k):
    distances = []
    for obj in trainingSet:
        dist = eucDistance(testInstance,obj,4)
        distances.append((obj,dist))
    findClosest = sorted(distances,key=lambda x: x[1])
    return [findClosest[k] for i in range(k)]        

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