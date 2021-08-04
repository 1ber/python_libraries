#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Copyright (c) 2021 Humberto Ramos Costa

import os, sys, random
from matplotlib import pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d
import mplcyberpunk, random

def generate_random_line( minimum=0, number=0, increase=0 ):
    values=[ minimum ]
    current=minimum
    for v in range( number-1 ):
        current=current + random.randint( 0, increase )
        values.append( current )
        
    return( values )
    
    
    


def main():

    ages_x = list( range(25, 35) )

    # ~ print( plt.style.available )
    # ~ ['seaborn-dark-palette', 'ggplot', 'seaborn-darkgrid', 'dark_background'
    # ~ , 'bmh', 'seaborn-pastel', 'seaborn-talk', 'tableau-colorblind10'
    # ~ , 'Solarize_Light2', 'seaborn-colorblind', 'seaborn-deep', 'seaborn-white'
    # ~ , 'seaborn-poster', 'seaborn-paper', 'seaborn', 'fivethirtyeight'
    # ~ , 'seaborn-ticks', 'seaborn-muted', '_classic_test', 'grayscale'
    # ~ , 'fast', 'seaborn-dark', 'seaborn-bright', 'classic', 'seaborn-whitegrid', 'seaborn-notebook']
    # ~ plt.style.use( 'Solarize_Light2' )
    # ~ plt.xkcd()


    # ~ plt.plot( ages_x, generate_random_line( 20000, 10, 200 ), color='#444444', linestyle='-', linewidth=3 )
    # ~ plt.plot( ages_x, generate_random_line( 20000, 10, 200 ), color='#444444', linestyle='--', linewidth=4  )
    # ~ plt.plot( ages_x, generate_random_line( 20000, 10, 200 ), color='#5a7d9a', linestyle='-.', linewidth=5   )
    # ~ plt.plot( ages_x, generate_random_line( 20000, 10, 200 ), color='#adad3b', linestyle=':', linewidth=6  )
    plt.style.use("cyberpunk")
    plt.ion()
    data_lists=[]
    for n in range( 10 ):
        # ~ plt.cla() # Clean
        # ~ plt.clf()
        l = generate_random_line( 20000, 10, 200 )
        ls=gaussian_filter1d(l, sigma=5)
        for i in range( len( ls ) ):
            plt.plot( ages_x[0:i], ls[0:i]  )
            plt.pause( 1 )

        # ~ data_lists.append( generate_random_line( 20000, 10, 200 ) )


        # ~ for l in data_lists:
            # ~ ls=gaussian_filter1d(l, sigma=5)
            # ~ for i in range( len( ls ) ):
                # ~ plt.plot( ages_x[0:i], ls[0:i]  )
                # ~ plt.pause( 1 )

        
    plt.ioff()
        
        
    # ~ plt.plot( ages_x, generate_random_line( 20000, 10, 200 ) )
    # ~ plt.plot( ages_x, generate_random_line( 20000, 10, 200 ) )
    # ~ plt.plot( ages_x, generate_random_line( 20000, 10, 200 ) )
    
    
    plt.grid( True )
    
    
    plt.show()
    
    
    sys.exit( 0 )

if __name__ == "__main__":

    main()
