import matplotlib.pyplot as plt
import numpy as np

########################################################### СТИЛЬ ЛИНИИ #################################################################

y = np.array([3,1,10,5,6,7])

#Для того чтобы поменять стиль линии нужно использовать ключевое слово linestyle или ls 
#Для изменения цвета линии используется ключевое слово color или c

#    Style	         Or
#'solid'(default)	'-'	
#'dotted'	        ':'	
#'dashed'	       '--'	
#'dashdot'	       '-.'	
#'None'	          '' or ' '

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
#Также можно менять ширину линии иcпользуя команду linewidth или lw

plt.plot(y, linestyle = 'dotted',lw = 10,color = 'r')

plt.show()