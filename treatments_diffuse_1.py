import numpy
import pylab
import scipy.stats, scipy
import matplotlib.pyplot as plt
import math

x = numpy.arange(-40, 40, 0.001)
def model(position, width, height):
    return  height * math.sqrt(2*math.pi) * width * scipy.stats.norm.pdf(x, position, width)
position = [0,0, 0, 0, 0]
height = [7.44, 7.37, 6.426,7.43,6.45]
width = [12.764,12.764, 12.764, 12.764,12.764]
legend = ["Virgin Brown Untreated","Shampoo with silicone","Shampoo + Conditioner with silicone", "Shampoo w/o silicone", "Shampoo + Conditioner w/o silicone"]
gauss = [0]*5

for i in range(5):
    gauss[i] = model(position[i], width[i], height[i])
    plt.plot(x,gauss[i],label=legend[i])

plt.legend(shadow=True, fancybox=True)
plt.xlabel("Angles (Degrees)")
plt.ylabel("Intensity (%)")
plt.title("Effect of chemical treatment on diffuse component")
plt.show()
