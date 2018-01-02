import numpy as np
from network import Network
from create_image import create_image
import matplotlib.pyplot as plt
from save_image import save_image
from calculate_output import calculate_output

##########################
network_name = "/home/csanna/PycharmProjects/lib_trp_0102_new/nets/lena.jpg"
# Image to draw on (needed for resolution
img3 = plt.imread('./lena.jpg')
img3 = img3 / 255

# [#columns, #rows]!!!!
res = [img3.shape[1], img3.shape[0]]
print(img3.shape)



#res = [201, 101]

mynet = Network(network_name)
layers = mynet.get_layers()

calculate_output(layers, res, 2)


img = create_image(mynet, [2], img=img3, res=res, plot_output=True)

all_outputs = mynet.get_all_output()

print(img.shape)
##############################################################
# # TEST save_image
print("\n****** SAVE_IMAGE ******\n")

save_image('./trial2.png', img)

##############################################################
# # Show the result
fig, ax = plt.subplots()
#ax[0].imshow(img3, cmap='gray', interpolation='nearest', origin='upper')
ax.imshow(img, cmap='gray' ,interpolation='nearest', origin='upper')
plt.show()