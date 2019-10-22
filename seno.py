import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,150)
y = np.cos(x)

plt.figure()
plt.plot(x,y)
plt.title("Gráfica función Seno")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("grafica_seno.png")
    
    
    
    
    
    