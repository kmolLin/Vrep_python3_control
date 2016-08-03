import math
from math import *



L1 = 135.0
L2 = 145.0

#X ,Y= 0,0

x = -189.443
y = -58.074

theate = float((x*x+y*y-L1*L1-L2*L2)/(2*L1*L2))

print(theate)
rad = math.acos(theate)
print(rad)
tha = math.degrees(rad)
#tha為算出來的角度
print("算出來的",tha)


###test==================


theatanr = math.acos(x/(math.sqrt(x*x+y*y)))
theatan = math.degrees(theatanr)
#theataN的角度
print("theatan角度",theatan)
theatalphar = math.acos((x*x+y*y+L1*L1-L2*L2)/(2*math.sqrt(x*x+y*y)*L1))

theatalpha = math.degrees(theatalphar)
#theatAlpha的角度
print("theatalpha角度",theatalpha)

#theata2 = theatan + theatAlpha
theata2 = theatan+theatalpha
print("theata2",theata2)
#theata3 = tha - theata2
theata3 = tha - theata2
print("theata3",theata3)


