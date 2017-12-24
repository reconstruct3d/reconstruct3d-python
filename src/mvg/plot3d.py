import numpy as np
#%matplotlib notebook
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from skimage.transform import resize

disparity=np.load('./disparity.npy')
factor=3
disparity = resize(disparity,output_shape=(disparity.shape[0]/factor, disparity.shape[1]/factor))

x,y=np.meshgrid(np.arange(disparity.shape[0]), np.arange(disparity.shape[1]))

fig= plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(xs=x.flatten(), ys=y.flatten(), zs=disparity.flatten(), color='r', marker='x')
plt.show()
