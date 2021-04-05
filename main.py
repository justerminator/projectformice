#python -i projectv1.py

from collections import defaultdict
from itertools import chain

animalLst = []
resultanimals = []
#input animal
k = 0
o = 0

while(True):
    animals = int(input("input animal list or 0 to end: "))
    if animals == 0:
        break;
    animalLst.append(animals)

for x in animalLst:
    k = x
    if k not in resultanimals:
        resultanimals.append(k)
    elif k in resultanimals:
        pass


#input duration


x = 0
result = 0
durationlst = []
while(True):
    x += 1
    duration = float(input("input duration or 0 to end: "))
    if duration == 0:
        break;
    #if x <= 4:
     #   result += duration
    #if x == 4:
    #    result = result / 4
     #   durationlst.append(result)
    #    x = 0
     #   result = 0
    durationlst.append(duration)

#newT = list(zip(animalLst, list(durationlst)))

#for avg dur

res = defaultdict(list)

for ani, dur in zip(animalLst, durationlst):
    res[ani].append(dur)

res2 = defaultdict(list)
for key1, value1 in res.items():
    intVal1 = sum(value1)
    intVal1 = intVal1 / 4
    res2[key1].append(intVal1)



#input distance
i = 0
result2 = 0
distancelst = []
while(True):
    i += 1
    distance = float(input("input distance or 0 to end: "))
    if distance == 0:
        break;
    #if i <= 4:
    #    result2 += distance
    #if i == 4:
    #    result2 = result2 / 4
    #    distancelst.append(result2)
    #    i = 0
    #    result2 = 0
    distancelst.append(distance)


#for avg dist
des = defaultdict(list)

for ani2, dist in zip(animalLst, distancelst):
    des[ani2].append(dist)

des2 = defaultdict(list)
for key2, value2 in des.items():
    intVal2 = sum(value2)
    intVal2 = intVal2 / 4
    des2[key2].append(intVal2)

print("Animals              Avg Duration          Avg Distance")
for printkey1, printkey2 in zip(res2, des2):
    print(str(printkey1) + "                     " + str(res2[printkey2])[1:-1] + "                 " + str(des2[printkey2])[1:-1])

lstResVal = []
lstResAni = []
for x,y in res2.items():
    lstResAni.append(x)
    lstResVal.append(y)

lstResVal2 = list(chain.from_iterable(lstResVal))
#lstResAni2 = list(chain.from_iterable(lstResAni))

lstDesVal = []
for x, y in des2.items():
    lstDesVal.append(y)

lstDesVal2 = list(chain.from_iterable(lstDesVal))

d_duration = dict(zip(lstResAni, lstResVal2))
d_distance = dict(zip(lstResAni, lstDesVal2))

#some tools
def maxDuration(d_duration):
    lstofr = []
    for x in d_duration:
        if d_duration[x] == 90:
            lstofr.append(x)
    return lstofr

#this may be useless actually....
def maxDistance(d_distance):
    lstofr2 = []
    lstofr3 = []
    p = 0
    for y in d_distance:
        if d_distance[y] > p:
            p = d_distance[y]
            lstofr2.append(y)
            lstofr3.append(p)
    intermD = dict(zip(lstofr2, lstofr3))

    return max(intermD, key=intermD.get)

def minDuration(d_duration):
    lstOfAn = []
    lstOfSmall = []
    for i in d_duration:
        lstOfAn.append(i)
        lstOfSmall.append(d_duration[i])
    intermDur = dict(zip(lstOfAn, lstOfSmall))
    return min(intermDur, key=intermDur.get)

def minDistance(d_distance):
    lstOfAnD = []
    lstOfSmallD = []
    for a in d_distance:
        lstOfAnD.append(a)
        lstOfSmallD.append(d_distance[a])
    intermDurD = dict(zip(lstOfAnD, lstOfSmallD))
    return min(intermDurD, key=intermDurD.get)

#shows max duration, distance avgs

print("Max dist")
print(maxDistance(d_distance))

print("Max duration (90)")
print(maxDuration(d_duration))

print("Min dist")
print(minDistance(d_distance))

print("Min Duration")
print(minDuration(d_duration))

#print(max(d_duration, key=d_duration.get))
#print(max(d_distance, key=d_distance.get))




