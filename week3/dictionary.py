import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
sin_dict={'s1':[1,2],'s2':[2,5],'s3':[3,8],'s4':[9,11],'s5':[10,13]}
k=input('enter sinosidelkey to generate:')
if sin_dict[k]:
	x=sin_dict[k][0]*np.sin(2*np.pi*sin_dict[k][1]*t)
	plt.plot(t,x)
	plt.show()
