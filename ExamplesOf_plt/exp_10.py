import numpy as np
import matplotlib.pyplot as plt

########################################################### Сетка #################################################################

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)

plt.title("EXAMPLE")
plt.xlabel("X")
plt.ylabel("Y")

#отображает сетку
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5) # параметры принимаемые функцией grid(color = 'color', linestyle = 'linestyle', linewidth = number,axis = 'x' или 'y').
#параметр axis отображает указаную ось сетки

plt.show()