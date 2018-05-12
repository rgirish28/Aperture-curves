import numpy
import pylab
import scipy.stats, scipy
import matplotlib.pyplot as plt
import math

x = numpy.arange(-40, 40, 0.001)
def model(position, width, height):
    return  height * math.sqrt(2*math.pi) * width * scipy.stats.norm.pdf(x, position, width)
position = [2.77,0, 0.74]
height = [82.085, 75.054,89.948 ]
width = [2.272,1.845, 3.094]
position1 = [-2.22,-2.01, -8]
height1 = [11.56, 11.786,7.052]
width1 = [4.189,4.289,2.291]
legend = ["Virgin Brown Untreated","Hairspray 1", "Hairspray 2"]
gauss = [0]*33
gauss1 = [0]*3

for i in range(3):
    gauss[i] = model(position[i], width[i], height[i])
    gauss1[i] = model(position1[i], width1[i], height1[i])
    
#plt.plot(x,gauss[0]+gauss[1]+gauss[2],label="Best fit",linewidth = 2.0)

for i in range(3):
    plt.plot(x,gauss1[i]+gauss[i],label=legend[i], linewidth = 2.0)


plt.legend(shadow=True, fancybox=True)
plt.xlabel("Angles (Degrees)")
plt.ylabel("Intensity (%)")
plt.title("Effect of hairspray on gloss")
plt.show()
