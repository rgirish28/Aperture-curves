import numpy
import pylab
import scipy.stats, scipy
import matplotlib.pyplot as plt
import math

x = numpy.arange(-40, 40, 0.001)
def model(position, width, height):
    return  height * math.sqrt(2*math.pi) * width * scipy.stats.norm.pdf(x, position, width)
position = [2.77,2.855, 2.57, 2.89,2.49]
height = [82.085, 84.86, 81.7252,84.917,79.03 ]
width = [2.272,2.30, 2.357, 2.3163,2.526 ]
position1 = [-2.22,-2.722, -2.506,-2.27 ,-2.35]
height1 = [11.56, 9.76, 9.82,10.10,10.6]
width1 = [4.189,4.067, 4.209, 4.289,4.289]
legend = ["Virgin Brown Untreated","Shampoo with silicone","Shampoo + Conditioner with silicone", "Shampoo w/o silicone", "Shampoo + Conditioner w/o silicone"]
gauss = [0]*5
gauss1 = [0]*5

for i in range(5):
    gauss[i] = model(position[i], width[i], height[i])
    gauss1[i] = model(position1[i], width1[i], height1[i])
    
#plt.plot(x,gauss[0]+gauss[1]+gauss[2],label="Best fit",linewidth = 2.0)

for i in range(5):
    plt.plot(x,gauss1[i]+gauss[i],label=legend[i], linewidth = 2.0)


plt.legend(shadow=True, fancybox=True)
plt.xlabel("Angles (Degrees)")
plt.ylabel("Intensity (%)")
plt.title("Effect of chemical treatment on gloss")
plt.show()
