#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import mplcyberpunk, random

def generate_random_line( minimum=0, number=0, increase=0 ):
    values=[ minimum ]
    current=minimum
    for v in range( number-1 ):
        current=current + random.randint( 0, increase )
        values.append( current )
        
    return( values )
    
    

plt.style.use("cyberpunk")

plt.plot( generate_random_line( minimum=0, number=10, increase=5 ) , marker='o')
plt.plot( generate_random_line( minimum=0, number=10, increase=2 ) , marker='o')
plt.plot( generate_random_line( minimum=0, number=10, increase=7 ) , marker='o')
plt.plot( generate_random_line( minimum=0, number=10, increase=3 ) , marker='o')
plt.plot( generate_random_line( minimum=0, number=10, increase=9 ) , marker='o')

# ~ mplcyberpunk.add_glow_effects()
mplcyberpunk.make_lines_glow()
# ~ mplcyberpunk.add_underglow()

plt.show()
