from numpy import *
import operator

def createDateSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]]) #样本,作为参考点
    labels=['A','A','B','B'] # 样本的标签
    return group,lables

def classify0(intX,dataset,labels,k):
    dataSetSize=dataSet.shape[0]     #shape()用于查看矩阵或者数组的维数
    diffMat=tile(inX,(dataSetSize,1))-dataset #tile重复dataSetSize数组一次 Eg:(4,1) 4行1列 默认包含一次 
    sqDiffMat=diffMat**2 #平方
    sortDistIdicies=distance.argsort() #排序 主要作用是对数组里的数字从小到大排序，取对应的序列值
    classCount=()
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]] #把序列值带入并选出对应的标签
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1 #做成字典标签
    sortedClassCount=sorted(classCount.iteritems,key=operator.itemgetter(1),reverse=True) #循环 Reverse从小到大 iteritems以字典形式返回 并提取第二个元素
    return sortedClassCount[0][0]  
    
    
