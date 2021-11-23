import numpy as np
import matplotlib.pyplot as plt

############################################################################################################################

y = np.array([3,1,10,5,6,7])

#Вы можете использовать ключевое слова markeredcolor или его сокращение mec , для того чтобы изменить цвет обводки маркера
#Также вы можете использовать markerfacecolor или mfc , для того чтобы задать цвет заливки маркера

#Color Syntax	Description
#    'r'	       Red	
#    'g'	       Green	
#    'b'	       Blue	
#    'c'	       Cyan	
#    'm'	       Magenta	
#    'y'	       Yellow	
#    'k'	       Black	
#    'w'	       White

#Также можно использовать цвет в формате HEX #bbb9d9

plt.plot(y,marker = 'o',mec = 'r',mfc ='w')

plt.show()