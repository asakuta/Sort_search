import math
import random

def bubble(values):
    iteration=len(values)
    while iteration > 0:
        for x in range(0, len(values)-1):
            if values[x] > values[x+1]:
                value1=values[x+1]
                value2=values[x]
                values[x]=value1
                values[x+1]=value2
        iteration=iteration-1
    print(values)

def callQ(values):
    result=Qsort(values)
    print(result)

def Qsort(values):
    if len(values) > 1:
        index=random.randint(0, len(values)-1)
        number=[values[index]]
        low=[]
        high=[]
        count=0
        for item in values:
            if item < values[index]:
                low.insert(len(low), item)
            if item > values[index]:
                high.insert(len(high), item)
            if item == values[index]:
                count=count+1
        if count > 1:
            for x in range(0, count-1):
                number.insert(len(number), values[index])
                x=x+1
        result=Qsort(low) + number + Qsort(high)
        return result
    else:
        return values

def insert(values):
    newList=[]
    newList.insert(0, values[0])
    for x in range(1, len(values)):
        number=values[x]
        result=binaryS(number, newList, newList)
        index=result[1]
        if result[0] is "after":
            newList.insert(index+1, number)
        if result[0] is "before":
            newList.insert(index, number)
    print(newList)

def binaryS(value, List, original):
    result=[]
    if len(List) > 1:
        index=math.ceil((len(List)-1)/2)
        focus=List[index]
        newList=[]
        position="after"
        if value > focus:
            for x in range(index+1, len(List)):
                newList.insert(len(newList), List[x])
        if value < focus:
            for x in range(0, index):
                newList.insert(len(newList), List[x])
                position="before"
        if value == focus or len(newList) == 0:
            result.insert(0, position)
            for x in range(0, len(original)):
                if original[x] is focus:
                    result.insert(1, x)
            return result
        return binaryS(value, newList, original)
    if len(List) == 1:
        number=List[0]
        if value >= number:
            for y in range(0, len(original)):
                if original[y] is number:
                    result=[]
                    result.insert(0, "after")
                    result.insert(1, y)
        if value < number:
            for y in range(0, len(original)):
                if original[y] is number:
                    result.insert(0, "before")
                    result.insert(1, y)
                    break
        return result

values=[138, 2, 24, 57, 57, 3]
bubble(values)
values=[138, 2, 24, 57, 57, 3]
callQ(values)
values=[138, 2, 24, 57, 57, 3]
insert(values)

    

