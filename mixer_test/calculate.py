import math
from math import *

def couclate(x,y,z):
	
	L1 = 135.0
	L2 = 145.0
	a1x = 145.0
	a1y = 0.0

	#X ,Y= 0,0

	#x = -189.443
	#y = -58.074

	##Y theata
	theataRoateRad = math.acos((a1x*x+a1y*y)/(a1x*math.sqrt(x*x+y*y)))
	print(theataRoateRad)
	theataRoate = math.degrees(theataRoateRad)
	print(theataRoate)
	theate = float((x*x+z*z-L1*L1-L2*L2)/(2*L1*L2))

	print(theate)
	rad = math.acos(theate)
	print(rad)
	tha = math.degrees(rad)
	#tha為算出來的角度
	print("算出來的",tha)


	#thn = arcos(x/(sqrt(x^2+y^2)))
	#tha = (x^2+y^2+L1^2+L2^2)/(2(sqrt(x^2+y^2)*L1))

	theatanr = math.acos(x/(math.sqrt(x*x+z*z)))
	theatan = math.degrees(theatanr)
	#theataN的角度
	print("theatan角度",theatan)
	theatalphar = math.acos((x*x+z*z+L1*L1-L2*L2)/(2*math.sqrt(x*x+z*z)*L1))

	theatalpha = math.degrees(theatalphar)
	#theatAlpha的角度
	print("theatalpha角度",theatalpha)

	#theata2 = theatan + theatAlpha
	theata2 = theatan+theatalpha
	print("theata2",theata2)
	#theata3 = tha - theata2
	theata3 = tha - theata2
	
	print("theata3",theata3)
	return(theata2,theataRoate,theata3)
	
X = 160
Y = 10
Z = 0
a,b,c = couclate(X,Y,Z)
print(a,b,c)