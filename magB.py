import numpy as np
import matplotlib.pyplot as plt

theta = [0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75]

magFDense = [np.sqrt(12**2+100+67**2), np.sqrt(14**2+16+64**2), np.sqrt(13**2+100+65**2),np.sqrt(4+100+66**2), np.sqrt(11**2+25+55**2), np.sqrt(4+55**2), np.sqrt(4+14**2+55**2), np.sqrt(13**2+14**2+58**2)]

plt.plot(theta, magFDense)
plt.title("Størrelsen på den magnetiske flukstettheten mot vinkelen theta.")
plt.xlabel("Vinkelen theta i radianer")
plt.ylabel("Størrelsen på den magnetiske flukstettheten i mikroT") 
plt.show()
