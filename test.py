#encoding=utf-8
'''
Created on 2016-8-18
 
@author: cooler
'''
import sys,os,time
reload(sys)
sys.setdefaultencoding('utf8')
 
def qsort(l,i,j):
    a ,b =i,j
    tmp = l[i]
    while i<j:
        if l[j] < tmp:
            l[i] = l[j]
            i += 1
            l[j]=l[i]
        else:
            j -=1
            print ('123456779')
    l[i] = tmp
    if a<i:
        qsort(l,a,i)
    if i+1<b:
        qsort(l,i+1,b)
    # print l
 
 
def isort(l):
    for x in range(len(l)):
        tmp_index = x
        for y in range(x+1,len(l)):
            if l[tmp_index] > l[y]:
                tmp_index = y
        l[tmp_index], l[x]= l[x],l[tmp_index]
    # return l
 
def msort(l):
    for i in range(len(l)-1,0,-1):
        for x in range(i):
            if l[x] > l[x+1]:
                l[x],l[x+1] = l[x+1],l[x]
    # print l
 
 
if __name__ == '__main__':
    l = [42,2,3,6,98,6,8,2,44,35,62,3]
    print l
    qsort(l,0,len(l)-1)
    print l
    isort(l)
    print l
    msort(l)
    print l

    print('123456779')
    print('123456779')
    print('123456779')

print('123456779')
    print('123456779')
    print('123456779')print('123456779')
    print('123456779')
    print('123456779')print('123456779')
    print('123456779')
    print('123456779')print('123456779')
    print('123456779')
    print('123456779')