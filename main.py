#python -i main.py

animalLst = []
animalLst_with_more_than_4_trials = []
#input animal
k = 0
o = 0

while(True):
    animals = int(input("input animal list or 0 to end: "))
    if animals == 0:
        break;
    if animals < k or animals > k:
        k = animals
        animalLst.append(k)
    elif animals == k:
        o += 1
        if o > 4:
            animalLst_with_more_than_4_trials.append(animals)
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
    if x <= 4:
        result += duration
    if x == 4:
        result = result / 4
        durationlst.append(result)
        x = 0
        result = 0



#input distance
i = 0
result2 = 0
distancelst = []
while(True):
    i += 1
    distance = float(input("input distance or 0 to end: "))
    if distance == 0:
        break;
    if i <= 4:
        result2 += distance
    if i == 4:
        result2 = result2 / 4
        distancelst.append(result2)
        i = 0
        result2 = 0
#interface

#while(True):
 #   userinput = input("Press 1 to display list of animals. Press 2 to display avg duration ")

print("Animal        Avg Duration           Avg Distance")
for (a, b, c) in zip(animalLst, durationlst, distancelst):

    print(str(a) + "              " + str(b) + "                       " + str(c))

d_duration = dict(zip(animalLst, durationlst))
d_distance = dict(zip(animalLst, distancelst))

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

