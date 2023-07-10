#swap first and last elements of the list
def changefirstandlast(list):
    size=len(list)
    temp1=list[0]
    temp2=list[size-1]
    list[0]=temp2
    list[size-1]=temp1

    return list

def sumList(list):
    sum=0
    for x in list:
        sum+=x
    avg=sum/len(list)

    newList=[sum,avg]

    return newList


#find duplicate elements in the list
def findDups(list):

    dupList=[]
    for i in range (len(list)):
        k=i+1
        for j in range (k, len(list)):
            if (list[i]==list[j] and (list[j] not in dupList)):
                dupList.append(list[i])
    return dupList
            
list1=[20,34,56,20,40,34]
    

print(changefirstandlast(list1))

print("sum of list is:{} and average is {}".format(sumList(list1)[0],sumList(list1)[1]))

print("Duplicate values in the list are",findDups(list1))