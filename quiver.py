'''
Matplotlib quiver
'''
import matplotlib.pyplot as plt
import numpy as np

def quiver():
    x = np.linspace(0,1,11)
    y = np.linspace(1,0,11)
    u = np.zeros((11,11))
    v = np.zeros((11,11))
    u[5,5] = 0.2
    v[5,5] = 0

    plt.figure()
    plt.quiver(x, y, u, v, scale=1)
    plt.show()

def radialDistortionPlot():
    
    x1 = np.linspace(-1,1,21)
    y1 = np.linspace(-1,1,21)

    x, y = np.meshgrid(x1, y1)

    r2 = np.add( np.multiply(x,x), np.multiply(y,y) )
    
    k = np.multiply( r2, 0.05 )
    
    u = np.multiply( x, k )
    v = np.multiply( y, k )

    fig = plt.figure()
    plt.quiver(x, y, u, v, scale=1)
    plt.draw()

    plt.pause(1)
    input("<Hit Enter To Close>")
    plt.close(fig)

radialDistortionPlot()
