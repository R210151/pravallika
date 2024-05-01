import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
F1=4
F2=2
x1=np.sin(2*np.pi*F1*t)
x2=np.sin(2*np.pi*F2*t)
c=x1+x2
plt.plot(c)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('sine wave')
plt.show()
