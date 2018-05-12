import numpy
import pylab
import scipy.stats, scipy
import matplotlib.pyplot as plt
import math

x = numpy.arange(-40, 40, 0.001)
def model(position, width, height):
    return  height * math.sqrt(2*math.pi) * width * scipy.stats.norm.pdf(x, position, width)
position = [0,0, 0]
height = [7.44, 2.748, 4.476]
width = [12.764,12.764, 12.764]
legend = ["Virgin Brown Untreated","Hairspray 1", "Hairspray 2"]
gauss = [0]*3

for i in range(3):
    gauss[i] = model(position[i], width[i], height[i])
    plt.plot(x,gauss[i],label=legend[i])

plt.legend(shadow=True, fancybox=True)
plt.xlabel("Angles (Degrees)")
plt.ylabel("Intensity (%)")
plt.title("Effect of hairsprays on diffuse component")
plt.show()
