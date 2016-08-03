import math

import matplotlib as plt


L1 = 135.0
L2 = 145.0

#X ,Y= 0,0


x = 40.0
y = 50.0

theate = float(x*x+y*y-L1*L1-L2*L2)/(2*L1*L2)
#為角度一
print(theate)
rad = math.acos(theate)
print(rad)
result = math.degrees(rad)
print(result)


###test==================


theata1 = 180.0 - result 
print("theata1大軸旋轉的角度",theata1)
thr = math.radians(theata1)
#為角度三
print("角度:+",theata1)
Bx = L1*math.sin(thr)
print("Bx:",Bx)
By = L1*math.cos(thr)

test = (math.fabs(math.fabs(x)-math.fabs(Bx)))/L2
print("結果",test)
rrad = math.acos(test)
theata2 = math.degrees(rrad)
print("小軸旋轉的角度",theata2)
#為角度二

