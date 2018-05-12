import numpy
import pylab
import scipy.stats, scipy
import matplotlib.pyplot as plt
import math

x = numpy.arange(-40, 40, 0.001)
def model(position, width, height):
    return  height * math.sqrt(2*math.pi) * width * scipy.stats.norm.pdf(x, position, width)
position = [-2.22,-2.722, -2.506,-2.27 ,-2.35]
height = [11.56, 9.76, 9.82,10.10,10.6]
width = [4.189,4.067, 4.209, 4.289,4.289]
legend = ["Virgin Brown Untreated","Shampoo with silicone","Shampoo + Conditioner with silicone", "Shampoo w/o silicone", "Shampoo + Conditioner w/o silicone"]
gauss = [0]*5

for i in range(5):
    gauss[i] = model(position[i], width[i], height[i])
    
#plt.plot(x,gauss[0]+gauss[1]+gauss[2],label="Best fit",linewidth = 2.0)
#plt.plot(x,gauss[0]+gauss[1],label="Gloss", linewidth = 2.0)

for i in range(5):
    plt.plot(x,gauss[i],label=legend[i])

plt.legend(shadow=True, fancybox=True)
plt.xlabel("Angles (Degrees)")
plt.ylabel("Intensity (%)")
plt.title("Effect of chemical treatment on chroma component")
plt.show()
