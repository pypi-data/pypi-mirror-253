#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  26 01:00:00 2024

@author: leahghartman
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from mpl_toolkits.axes_grid1 import make_axes_locatable

#########################
### START OF FUNCTIONS
#########################

def check_array(imgpath, imgar):
    """ Returns the image path or the array of the image based on what the user has input into the function that's calling check_array().

        Parameters
        ----------
        imgpath : string
            The path to the image that the user wants to run through the median filter.
        imgar : array
            Array of the image if the user wants to input an array into the function rather than just an image path.
    """
    # if the length of the image array is empty (the user didn't want to use an array), we use the image path instead
    if len(imgar) == 0:
        return(np.array(Image.open(imgpath).convert("L")))
    # if the length of the image array isn't zero, the user wants to use an array instead of the image path, so we return the array that was input
    else:
        return(imgar)

########################################################

def find_centroid(imgpath='', imgar=[]):
    """ Returns x- and y-coordinate of the centroid based on the MAXIMUM INTENSITY of the image in each transverse dimension.

        Parameters
        ----------
        imgpath (OPTIONAL) : string
            The path to the image that the user wants to run through the median filter.
        imgar (OPTIONAL) : array
            Array of the image if the user wants to input an array into the function rather than just an image path.
    """
    # set the array of the image to whatever the user specifies (either based on the image path OR an array that the user inputs)
    arrayimg = check_array(imgpath, imgar)

    # find the x- and y-coordinates of the centroid by doing a projection of the entire image and finding the maximum value in the array for each dimension
    centx, centy = np.argmax(arrayimg.sum(axis=0)), np.argmax(arrayimg.sum(axis=1))

    # return the centroid's coordinates
    return(centx, centy)

########################################################

def find_proj_x(imgpath='', imgar=[]):
    """ Returns the projection of an image along the x-axis.

        Parameters
        ----------
        imgpath (OPTIONAL) : string
            The path to the image that the user wants to run through the median filter.
        imgar (OPTIONAL) : array
            Array of the image if the user wants to input an array into the function rather than just an image path.
    """
    # set the array of the image to whatever the user specifies (either based on the image path OR an array that the user inputs)
    arrayimg = check_array(imgpath, imgar)

    # return the summation of EACH column (so, this is the projection along the x-axis)
    return(arrayimg.sum(axis=0))

########################################################

def find_proj_y(imgpath='', imgar=[]):
    """ Returns the projection of an image along the y-axis.

        Parameters
        ----------
        imgpath (OPTIONAL) : string
            The path to the image that the user wants to run through the median filter.
        imgar (OPTIONAL) : array
            Array of the image if the user wants to input an array into the function rather than just an image path.
    """
    # set the array of the image to whatever the user specifies (either based on the image path OR an array that the user inputs)
    arrayimg = check_array(imgpath, imgar)
    
    # return the summation of EACH row (so, this is the projection along the y-axis)
    return(arrayimg.sum(axis=1))

########################################################

def find_line_x(xpixel, imgpath='', imgar=[], toavg=0):
    """ Returns the lineout of an image along the x-axis and averages multiple columns of pixels if the user wants.

        Parameters
        ----------
        xpixel : integer
            Specifies at what COLUMN the user wants to take the lineout along the image in pixels.
        imgpath (OPTIONAL) : string
            The path to the image that the user wants to run through the median filter.
        imgar (OPTIONAL) : array
            Array of the image if the user wants to input an array into the function rather than just an image path.
        toavg (OPTIONAL) : integer
            Specifies the number of pixels on EACH SIDE of the original pixel lineout the user wants to create a projection with (so, center lineout, plus 
            two lineouts on either side if "toavg" is set equal to 2.
    """
    # set the array of the image to whatever the user specifies (either based on the image path OR an array that the user inputs)
    arrayimg = check_array(imgpath, imgar)

    # this isn't really needed functionality, but added a while loop that appends the all the lineouts the user wants to a list
    lineoutar = []
    i = -toavg;
    while i <= toavg:
        lineoutar.append(np.array(arrayimg[xpixel+i, :]))
        i += 1;

    # return the total projection of all of the lineouts
    return(np.array(lineoutar).sum(axis=0))

########################################################

def find_line_y(ypixel, imgpath='', imgar=[], toavg=0):
    """ Returns the lineout of an image along the y-axis and averages multiple columns of pixels if the user wants.

        Parameters
        ----------
        ypixel : integer
            Specifies at what ROW the user wants to take the lineout along the image in pixels.
        imgpath (OPTIONAL) : string
            The path to the image that the user wants to run through the median filter.
        imgar (OPTIONAL) : array
            Array of the image if the user wants to input an array into the function rather than just an image path.
        toavg (OPTIONAL) : integer
            Specifies the number of pixels on EACH SIDE of the original pixel lineout the user wants to average with (so, center lineout, plus two lineouts on
            either side if "toavg" is set equal to 2.
    """
    # set the array of the image to whatever the user specifies (either based on the image path OR an array that the user inputs)
    arrayimg = check_array(imgpath, imgar)

    # this isn't really needed functionality, but added a while loop that appends the all the lineouts the user wants to a list
    lineoutar = []
    i = -toavg;
    while i <= toavg:
        lineoutar.append(np.array(arrayimg[:, ypixel+i]))
        i += 1;

    # return the total projection of all of the lineouts
    return(np.array(lineoutar).sum(axis=0))

########################################################

def sum_intensity_prof(imgpath='', imgar=[], lineout=False, xpixel=0, ypixel=0, toavg=0):
    """ Returns the lineout of an image along the y-axis and averages multiple columns of pixels if the user wants.

        Parameters
        ----------
        xpixel : integer
            Specifies at what ROW the user wants to take the lineout along the image in pixels.
        imgpath (OPTIONAL) : string
            The path to the image that the user wants to run through the median filter.
        imgar (OPTIONAL) : array
            Array of the image if the user wants to input an array into the function rather than just an image path.
        toavg (OPTIONAL) : integer
            Specifies the number of pixels on EACH SIDE of the original pixel lineout the user wants to average with (so, center lineout, plus two lineouts on
            either side if "toavg" is set equal to 2.
    """
    # set the array of the image to whatever the user specifies (either based on the image path OR an array that the user inputs)
    arrayimg = check_array(imgpath, imgar)

    # find the width and height of the image
    imheight, imwidth = np.shape(arrayimg)

    # create a numpy array so the axes will actually work on the right-hand-side graph (this isn't necessary on the top graph)
    positionsy = np.arange(1, imheight + 1, 1)
    positionsx = np.arange(1, imwidth + 1, 1)

    # customize the plots/plot as a whole (that is literally all that these lines of code do)
    fig, main_ax = plt.subplots(figsize=(7, 7))
    divider = make_axes_locatable(main_ax)
    top_ax = divider.append_axes("top", 1.05, pad=0.3, sharex=main_ax)
    right_ax = divider.append_axes("right", 1.05, pad=0.3, sharey=main_ax)

    # make the tick labels on the bottom sides of the top- and right-hand-side graphs disappear
    top_ax.xaxis.set_tick_params(labelbottom=False)
    right_ax.yaxis.set_tick_params(labelleft=False)
    right_ax.tick_params(labelrotation=-90)

    # give labels to all of the necessary axes and plots themselves (might have to play with the arangement of the right plot's title)
    main_ax.set_xlabel('x pixels', fontsize=13)
    main_ax.set_ylabel('y pixels', fontsize=13)
    top_ax.set_title('Intensity Profile (Projection) of Pixel Columns', fontsize=13)
    right_ax.set_title('Intensity Profile (Projection) of Pixel Rows', x=1.13, y=-0.05, rotation=-90, fontsize=13)

    # show the image as the main plot
    main_ax.imshow(arrayimg, extent=[0, imwidth, 0, imheight])

    # calculates the sum of the intensity values of all the pixels in every row and column
    cols = find_proj_x(imgar=arrayimg)
    rows = find_proj_y(imgar=arrayimg)

    # plots the right and top graphs with certain colors. If you want a different color, just change the 'color' input below
    v_prof, = right_ax.plot(rows, positionsy, color='black')
    h_prof, = top_ax.plot(cols, color='black')

    # show the entire figure
    plt.autoscale()
    plt.show()