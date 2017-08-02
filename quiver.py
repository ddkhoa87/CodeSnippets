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
    
    x1 = np.linspace(-1,1,31)
    y1 = np.linspace(-1,1,31)

    x, y = np.meshgrid(x1, y1)

    r2 = np.add( np.multiply(x,x), np.multiply(y,y) )
    
    # Multiplied by >0 -> barrel, <0 -> pincushion

    fig = plt.figure(1, figsize=(13,5))
    
    # Pincushion
    k = np.multiply( r2, -0.03 )
    
    u = np.multiply( x, k )
    v = np.multiply( y, k )

    fig1 = plt.subplot("121")
    fig1.set_title('k < 0')
    plt.quiver(x, y, u, v, scale=1)

    # Barrel
    k = np.multiply( r2, 0.03 )
    
    u = np.multiply( x, k )
    v = np.multiply( y, k )

    fig2 = plt.subplot(122)
    fig2.set_title('k > 0')
    plt.quiver(x, y, u, v, scale=1)

    # Draw two figures
    plt.draw()

    plt.pause(1)
    input("<Hit Enter To Close>")
    plt.close(fig)

def drawMeshes():
    x1 = np.linspace(-1,1,31)
    y1 = np.linspace(-1,1,31)

    x, y = np.meshgrid(x1, y1)

    r2 = np.add( np.multiply(x,x), np.multiply(y,y) )
    
    # Multiplied by >0 -> barrel, <0 -> pincushion

    fig = plt.figure(2, figsize=(13,5))
    
    # Pincushion
    fig1 = plt.subplot("121")
    fig1.set_title('Original')
    plt.scatter(x, y, s = 2)

    # Barrel
    k = np.multiply( r2, -0.2 )
    
    u = np.multiply( x, k )
    v = np.multiply( y, k )

    fig2 = plt.subplot(122)
    fig2.set_title('k < 0')

    # Make some adjust ment
    #u = np.add(u, 0.5)
    #v = np.add(v, 0.5)

    #plt.scatter( u[10:20], v[10:20], s = 2)
    plt.scatter( np.add(x, u), np.add(y, v), s = 2)

    # save to txt
    np.savetxt('x', x, fmt='%.1f')
    np.savetxt('u', u, fmt='%.1f')

    # Draw two figures
    plt.draw()

    plt.pause(1)
    input("<Hit Enter To Close>")
    plt.close(fig)

radialDistortionPlot()
drawMeshes()
