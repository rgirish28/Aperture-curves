import numpy
import pylab
import scipy.stats, scipy
import matplotlib.pyplot as plt
import math

x = numpy.arange(-40, 40, 0.001)
def model(position, width, height):
    return  height * math.sqrt(2*math.pi) * width * scipy.stats.norm.pdf(x, position, width)
position = [-2.22,-4.42, -4.12, -4.33]
height = [11.56, 28.70, 24.98,5.432]
width = [4.189,4.289, 4.289, 1.945]
legend = ["Virgin Brown","Bleached","Bleached - Red Dyed", "Bleached - Black Dyed"]
gauss = [0]*4

for i in range(4):
    gauss[i] = model(position[i], width[i], height[i])
    
#plt.plot(x,gauss[0]+gauss[1]+gauss[2],label="Best fit",linewidth = 2.0)
#plt.plot(x,gauss[0]+gauss[1],label="Gloss", linewidth = 2.0)

for i in range(4):
    plt.plot(x,gauss[i],label=legend[i])

plt.legend(shadow=True, fancybox=True)
plt.xlabel("Angles (Degrees)")
plt.ylabel("Intensity (%)")
plt.title("Effect of change in colour on chroma component")
plt.show()
