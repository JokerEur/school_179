import numpy as np
import matplotlib.pyplot as plt

########################################################### Лэйблы и загловление #################################################################

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)

#Вы можете добавлять загловление используя функцияю title()
#Название для оси X используя функцию xlable()
#Название для оси Y используя функцию ylable()

plt.title("EXAMPLE")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
