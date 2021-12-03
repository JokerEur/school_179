import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

# равёртка реализуется в строках и столбцах
# Первый аргумен - столбец, второй аргумен - сторока
# Третий аргумент - показывает над каким plot'ом мы совершаем преобразования
plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()