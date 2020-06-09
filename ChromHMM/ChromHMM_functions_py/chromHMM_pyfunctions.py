#!/data/manke/group/ferrari/anaconda3/bin/python3

import math

def bin_region_size(lista, bin_size):

    '''
    This function takes as input a list of the format [chr, start, end] and a bin size (int)
    and returns a list of lists with the coordinates of the binned region
    '''

    out_lista=[]

    n_bins = (int(lista[2])-int(lista[1]))/bin_size
    start = int(lista[1])
    end = int(lista[1]) + bin_size
    out_lista.append([lista[0], start, end])
    for i in range(int(n_bins - 1)):
        out_lista.append([lista[0],out_lista[-1][2],out_lista[-1][2]+bin_size])
    if (int(lista[2])-int(lista[1]))%bin_size == 0:
        pass
        #print('Warning! The chosen bin size does not match the segmentation bin size')
        #exit(1)

    return out_lista


def bin_region_number(lista, numb_of_bins):
    
    '''
    This function takes as input a list of the format [chr, start, end] and the number of bins you want (int)
    and returns a list of lists with the coordinates of the binned region
    '''
    
    out_lista = []
    
    bin_size = float((int(lista[2])-int(lista[1]))/numb_of_bins)
    start = int(lista[1])
    end = int(lista[1]) + bin_size
    out_lista.append([lista[0], start, end, 1])
    for i in range(int(numb_of_bins - 1)):
        out_lista.append([lista[0],out_lista[-1][2],out_lista[-1][2]+bin_size,out_lista[-1][-1]+1])
    
    return out_lista



def compute_overlap(lista1,lista2):
    
    '''
    This function takes as input two lists of the form [chr, start, end] and returns the 
    '''
    # check if the format of input lists are valid
    try:
        lista1 = [lista1[0]]+[int(j) for j in lista1[1:]]
        lista2 = [lista1[0]]+[int(j) for j in lista2[1:]]
    except:
        print("The coordinates you provided are not valid. Exiting")
        return None
        exit(1)
    if lista1[1] > lista1[2] or lista2[1] > lista2[2]:
        print("The coordinates you provided are not valid. Exiting")
        return None
        exit(1)
    
    # check if regions overlap
    bol = True
    if lista1[0] == lista2[0]:
        if lista1[2] <= lista2[1] or lista1[1] >= lista2[2]:
            bol = False
            overlap = 0
    else:
        bol = False
        overlap = 0 
    
    # if they overlap, compute overlap
    if bol: 
        if lista1[1] < lista2[1] and lista1[2] > lista2[1] and lista1[2] <= lista2[2]:
            overlap = lista1[2] - lista2[1]
        elif lista1[1] >= lista2[1] and lista1[2] <= lista2[2]:
            overlap = lista1[2]-lista1[1]
        elif lista1[1] >= lista2[1] and lista1[1] < lista2[2] and lista1[2] > lista2[2]:
            overlap = lista2[2] - lista1[1]
        elif lista1[1] < lista2[1] and lista1[2] > lista2[2]:
            overlap = lista2[2] - lista2[1]
    
    return overlap 
    
    

