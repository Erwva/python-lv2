import numpy as np
import matplotlib.pyplot as plt
img = plt.imread("tiger.png")
img = img[:,:,0].copy()
h=len(img)
w=len(img[0])
h,w = img.shape
print(h)
print(w)
plt.figure(1)
plt.imshow(img, cmap="gray")
for x in range(len(img)):
    for y in range(len(img[0])):
        img[x][y] = img[x][y]*2
        if(img[x][y]>1):
            img[x][y]=1.5
img_rot = np.zeros((w,h))
for x in range(0,h):
    img_rot[:,h-1-x]=img[x,:]

img = img_rot
img_fl = np.zeros((w,h))
for x in range(0,h):
    img_fl[:,x]= img[:,h-1-x]

img_resize = np.zeros((w,h))
for x in range(0,h):
    for y in range(0,w):
        img_resize = img[::10,::10]

img_cut = np.zeros((w,h))
for x in range(int (h/4), int (h/2)):
    img_cut[:,x]=img[:,x]






print(img.shape)
print(img.dtype)
plt.figure(2)
plt.imshow(img_resize, cmap="gray")
plt.figure(3)
plt.imshow(img_rot, cmap="gray")
plt.figure(4)
plt.imshow(img_fl, cmap="gray")
plt.figure(5)
plt.imshow(img_cut, cmap="gray")
plt.show()
