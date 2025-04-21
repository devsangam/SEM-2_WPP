import numpy as np
import math
import random
cartesian=np.zeros((10,2))
polar=np.zeros((10,2))

def cartesian_to_polar(point):
    r=math.sqrt(point[0]^2 +point[1]^2)
    if(not point[0]):
        return (r, (math.pi/2)*180)
    angle=math.atan(point[1]/point[0])
    return (r, (angle/math.pi)*180)
for i in range(10):
    x=random.randrange(0,100)
    y=random.randrange(0,100)
    cartesian[i]=(x,y)
    polar[i]= cartesian_to_polar((x,y))
    print()
    print("Cartesian:\nx = ",cartesian[i][0], ", y = ", cartesian[i][1])
    print("Polar:\nr = ",polar[i][0], ", θ =", str(polar[i][1])+"°")