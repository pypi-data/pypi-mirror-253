#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  26 01:00:00 2024

@author: leahghartman
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage

#########################
### START OF FUNCTIONS
#########################

def thru_median(imgpath, mediansize, repeatamount=0):
    """ Returns an image in the form of an array that has been run through a median filter a specified number of times.
    
        Parameters
        ----------
        imgpath : string
            The path to the image that the user wants to run through the median filter.
        mediansize : integer
            The size of the median filter in pixels (generally want this to be small; from 2-10 pixels).
        repeatamount (OPTIONAL) : integer
            The number of times the user wants to run the image through the median filter.
    """
    # use the specified image path to create an image object using PIL (Pillow)
    image = np.array(Image.open(imgpath).convert('L'))

    # create an array for the median filter images and append to this array when a change to the image is made
    result = [ndimage.median_filter(np.array(image), size=mediansize)]

    # for loop to repeat the number of times the median filter is run over the image
    for i in range(2, repeatamount+1):
        result.append(ndimage.median_filter(result[i-2], size=mediansize))

    # return the result after running through the median filter
    return(result[-1])

########################################################

def plot_median(imgpath, mediansize, repeatamount=0, clmap='plasma', fontsize=15):
    """ Returns a plot of the image before and after it has been run through the median filter a specified number of times.

        Parameters
        ----------
        imgpath : string
            The path to the image that the user wants to run through the median filter.
        mediansize : integer
            The size of the median filter in pixels (generally want this to be small; from 2-10 pixels).
        repeatamount (OPTIONAL) : integer
            The times the user wants the filter to be run over the image.
        clmap (OPTIONAL) : string
            The colormap that the user wants to use for the plots. This MUST be a colormap given by the matplotlib package.
        fontsize (OPTIONAL) : integer
            The fontsize used for the title of the plot. The axes labels are automatically formatted based on this number.
    """
    # get the image before the median filter is applied and after the filter is applied
    before = np.array(Image.open(imgpath).convert('L'))
    after = np.array(thru_median(imgpath, mediansize, repeatamount))

    # plot both images with before filtering on the left and after the filtering on the right; add in some nice settings
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.5, 3))

    # set the title and axes labels for the image
    ax1.set_title('Image Before Median Filter', fontsize=fontsize)
    ax2.set_title('Image After Median Filter', fontsize=fontsize)
    ax1.set_ylabel('y pixels', fontsize=fontsize-3)
    ax1.set_xlabel('x pixels', fontsize=fontsize-3)
    
    ax2.set_ylabel('y pixels', fontsize=fontsize-3)
    ax2.set_xlabel('x pixels', fontsize=fontsize-3)

    # show the images
    ax1.imshow(before, cmap=clmap)
    ax2.imshow(after, cmap=clmap)

########################################################

def thru_lowpass(imgpath, radius, imgar=[]):
    """ Returns an image in the form of an array that has been run through a low-pass filter one time.

        Parameters
        ----------
        imgpath : string
            The path to the image that the user wants to run through the median filter.
        radius : integer
            The radius of the mask used for the low-pass filter in pixels.
        isArray (OPTIONAL) : boolean
            Allows the user to also input an array (rather than a path string) by setting this to TRUE.
        arimg (OPTIONAL) : array
            Array input for the image if isArray is set to TRUE.
    """
    # make the image given at the path into an array
    if len(imgar) == 0:
        arrayimage = np.array(Image.open(imgpath).convert('L'))
    else:
        arrayimage = imgar

    #perform the fourier transform and save the complex output
    ft = np.fft.fft2(arrayimage, axes=(0,1))

    # shift the origin to the center of the image
    ft_shift = np.fft.fftshift(ft)

    # create circular mask using size specified in the cell above
    mask = np.zeros_like(arrayimage) # --> returns an array of zeros the same shape as the image
    cy = mask.shape[0] // 2
    cx = mask.shape[1] // 2
    cv2.circle(mask, (cx,cy), radius, (255,255,255), -1)[0]

    # blur the mask to prevent artifacts on the image
    finalmask = cv2.GaussianBlur(mask, (19,19), 0)

    # apply the mask to the shifted fourier transform of the image
    masked_ft_shifted = np.multiply(ft_shift,finalmask) / 255

    # shift origin from center to upper left corner (basically return the image to its original state before using fft to get back)
    back_ishift_masked = np.fft.ifftshift(masked_ft_shifted)

    # do inverse fft and save as complex output
    filteredimg = np.fft.ifft2(back_ishift_masked, axes=(0,1))

    # combine complex real and imaginary components to form (the magnitude for) the original image again
    filteredimg = np.abs(filteredimg).clip(0,255).astype(np.uint8)

    # return the filtered image
    return(filteredimg)

########################################################

def plot_lowpass(imgpath, radius, clmap='plasma', fontsize=15):
    """ Returns a plot of the image before and after it has been run through a low-pass filter one time.

        Parameters
        ----------
        imgpath : string
            The path to the image that the user wants to run through the median filter.
        radius : integer
            The radius of the mask used for the low-pass filter in pixels.
        clmap (OPTIONAL) : string
            The colormap that the user wants to use for the plots. This MUST be a colormap given by the matplotlib package.
        fontsize (OPTIONAL) : integer
            The fontsize used for the title of the plot. The axes labels are automatically formatted based on this number.
    """
    # get the image before the low-pass filter is applied and after the filter is applied
    before = np.array(Image.open(imgpath).convert('L'))
    after = np.array(thru_lowpass(imgpath, radius))

    # plot both images with before filtering on the left and after the filtering on the right; add in some nice settings
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.5, 3))

    # set the title and axes labels for both plots/images
    ax1.set_title('Image Before Low-Pass Filter', fontsize=fontsize)
    ax1.set_ylabel('y pixels', fontsize=fontsize-3)
    ax1.set_xlabel('x pixels', fontsize=fontsize-3)

    ax2.set_title('Image After Low-Pass Filter', fontsize=fontsize)
    ax2.set_ylabel('y pixels', fontsize=fontsize-3)
    ax2.set_xlabel('x pixels', fontsize=fontsize-3)

    # show the images
    ax1.imshow(before, cmap=clmap)
    ax2.imshow(after, cmap=clmap)

########################################################

def thru_medandlow(imgpath, mediansize, radius, repeatamount=0):
    """ Returns an image in the form of an array that has been run first through a median filter and then through a low-pass filter.

        Parameters
        ----------
        imgpath : string
            The path to the image that the user wants to run through the median filter.
        mediansize : integer
            The size of the median filter in pixels (generally want this to be small; from 2-10 pixels).
        radius : integer
            The radius of the mask used for the low-pass filter in pixels.
        repeatamount (OPTIONAL) : integer
            The times the user wants the MEDIAN filter to be run over the image.
    """
    # get the original image, the image after the median filter, and the image after both filters (median first, low-pass second)
    original = np.array(Image.open(imgpath).convert('L'))
    aftermed = np.array(thru_median(imgpath, radius))
    afterboth = np.array(thru_lowpass(aftermed, radius, isarray=True, arimg=aftermed))

    # return the array of the image after both filters have been applied
    return(afterboth)

########################################################

def plot_medandlow(imgpath, mediansize, radius, repeatamount=0, clmap='plasma', fontsize=15):
    """ Returns a plot of the original image, the image after ONLY a median filter has been applied, the image after ONLY a low-pass filter has been applied, and
        the image after BOTH a median filter and low-pass filter have been applied.

        Parameters
        ----------
        imgpath : string
            The path to the image that the user wants to run through the median filter.
        mediansize : integer
            The size of the median filter in pixels (generally want this to be small; from 2-10 pixels).
        radius : integer
            The radius of the mask used for the low-pass filter in pixels.
        repeatamount (OPTIONAL) : integer
            The times the user wants the MEDIAN filter to be run over the image.
        clmap (OPTIONAL) : string
            The colormap that the user wants to use for the plots. This MUST be a colormap given by the matplotlib package.
        fontsize (OPTIONAL) : integer
            The fontsize used for the title of the plot. The axes labels are automatically formatted based on this number.
    """
    # get the original image, the image after the median filter, the image after the low-pass filter, and the image after both filters
    original = np.array(Image.open(imgpath).convert('L'))
    aftermed = np.array(thru_median(imgpath, radius))
    afterlow = np.array(thru_lowpass(imgpath, radius))
    afterboth = np.array(thru_lowpass(aftermed, radius, isArray=True, arimg=aftermed))
    
    # create a figure with four subplots, show the images that are found above, and label each of them
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle('Original Image Compared to Combinations of Filters', fontsize=fontsize, y=1.01)
    ax1.imshow(original, cmap=clmap)
    ax1.set_title('Original Image', fontsize=fontsize-3)
    ax2.imshow(aftermed, cmap=clmap)
    ax2.set_title('After Median Filter', fontsize=fontsize-3)
    ax3.imshow(afterlow, cmap=clmap)
    ax3.set_title('After Low-Pass Filter', fontsize=fontsize-3)
    ax4.imshow(afterboth, cmap=clmap)
    ax4.set_title('After Both Filters', fontsize=fontsize-3)

    # label all x- and y-axes
    fig.text(0.5, 0.04, 'x pixels', ha='center', fontsize=fontsize-3)
    fig.text(0.04, 0.5, 'y pixels', va='center', rotation='vertical', fontsize=fontsize-3)

    # fix the axes ticks so they only show for outer plots
    for ax in fig.get_axes():
        ax.label_outer()
        