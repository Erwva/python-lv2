import numpy as np
import matplotlib.pyplot as plt


img_black = np.zeros((50,50))
img_white = 255*np.ones((50,50))

w,h = 100,100
for i in range(0,w):
    img = np.hstack((img_black,img_white))
    img_a=img.copy()
    img = np.hstack((img,img_a))
    
for i in range(0,h):
    img = np.vstack((img_white,img_black))
    img_b=img.copy()
    img = np.vstack((img,img_b))
    

plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()
