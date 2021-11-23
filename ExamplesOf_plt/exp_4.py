import numpy as np
import matplotlib.pyplot as plt

######################################################## МАРКЕРЫ ############################################################

# Marker	Description

#  'o'	     Circle	
#  '*'	     Star	
#  '.'	     Point	
#  ','	     Pixel	
#  'x'	     X	
#  'X'	     X (filled)	
#  '+'	     Plus	
#  'P'	     Plus (filled)	
#  's'	     Square	
#  'D'	     Diamond	
#  'd'	     Diamond (thin)	
#  'p'	     Pentagon	
#  'H'	     Hexagon	
#  'h'	     Hexagon	
#  'v'	     Triangle Down	
#  '^'	     Triangle Up	
#  '<'	     Triangle Left	
#  '>'	     Triangle Right	
#  '1'	     Tri Down	
#  '2'	     Tri Up	
#  '3'	     Tri Left	
#  '4'	     Tri Right	
#  '|'	     Vline	
#  '_'	     Hline

y = np.array([3,1,10,5,6,7])

#вы можете использовать ключевое слово marker , для того чтобы выделить точку специальным знаком

plt.plot(y,marker = 'o') # или marker = 'x'

plt.show()