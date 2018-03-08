from numpy import *
import operator

def createDateSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group,lables

def classify0(intX,dataset,labels,k):
    dataSetSize=dataSet.shape[0]     #shape()用于查看矩阵或者数组的维数
    diffMat=tile(inX,(dataSetSize,1))-dataset #tile重复dataSetSize数组一次 Eg:(4,1) 4行1列 包括自己
    sqDiffMat=diffMat**2 #平方
    sortDistIdicies=distance.argsort()
    classCount=()
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.iteritems,key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]  
    
    
