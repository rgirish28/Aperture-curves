import numpy
import pylab
import scipy.stats, scipy
import matplotlib.pyplot as plt
import math

x = numpy.arange(-40, 40, 0.001)
def model(position, width, height):
    return  height * math.sqrt(2*math.pi) * width * scipy.stats.norm.pdf(x, position, width)
position = [2.77,2.674, 2.56, 2.89]
height = [82.085, 50.74, 56.35,89.86]
width = [2.272,2.383, 2.343, 2.563]
position1 = [-2.22,-4.42, -4.12, -4.33]
height1 = [11.56, 28.70, 24.98,5.432]
width1 = [4.189,4.289, 4.289, 1.945]
legend = ["Virgin Brown","Bleached","Bleached - Red Dyed", "Bleached - Black Dyed"]
gauss = [0]*4
gauss1 = [0]*4

for i in range(4):
    gauss[i] = model(position[i], width[i], height[i])
    gauss1[i] = model(position1[i], width1[i], height1[i])
    
#plt.plot(x,gauss[0]+gauss[1]+gauss[2],label="Best fit",linewidth = 2.0)

for i in range(4):
    plt.plot(x,gauss1[i]+gauss[i],label=legend[i], linewidth = 2.0)


plt.legend(shadow=True, fancybox=True)
plt.xlabel("Angles (Degrees)")
plt.ylabel("Intensity (%)")
plt.title("Effect of change in colour on gloss")
plt.show()
