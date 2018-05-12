import numpy
import pylab
import scipy.stats, scipy
import matplotlib.pyplot as plt
import math

x = numpy.arange(-40, 40, 0.001)
def model(position, width, height):
    return  height * math.sqrt(2*math.pi) * width * scipy.stats.norm.pdf(x, position, width)
position = [0,0, 0, 0]
height = [7.44, 17.30, 16.54,5.31]
width = [12.764,12.764, 12.764, 12.764]
legend = ["Virgin Brown","Bleached","Bleached - Red Dyed", "Bleached - Black Dyed"]
gauss = [0]*4

for i in range(4):
    gauss[i] = model(position[i], width[i], height[i])
    plt.plot(x,gauss[i],label=legend[i])

plt.legend(shadow=True, fancybox=True)
plt.xlabel("Angles (Degrees)")
plt.ylabel("Intensity (%)")
plt.title("Effect of change in colour on diffuse component")
plt.show()
