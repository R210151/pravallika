import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.1)
f=2
x=np.sin(1*np.pi*f*t)
plt.plot(t,x)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('sine wave')
plt.show()
