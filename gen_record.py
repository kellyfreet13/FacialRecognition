#! /usr/bin/env python3
# -*-coding: utf-8-*-

__author__ = 'Moonkie'

import numpy as np
import cv2
import pandas as pd
import random
import os

curdir = os.path.abspath(os.path.dirname(__file__))

def gen_record(channel):
    target = pd.read_csv("train_target.csv",delimiter=',',dtype='a')
    data = pd.read_csv("train_data.csv",delimiter=',',dtype='a')
    labels = np.array(target,np.float)
    imagebuffer = np.array(data)
    images = np.array([np.array(image,dtype=np.uint8) for image in imagebuffer])
    del imagebuffer
    num_shape = int(np.sqrt(images.shape[-1]))
    images.shape = (images.shape[0],num_shape,num_shape)
    data = zip(labels, images)
    count = 0;
    for d in data:
        if count == 0:
            dest = os.path.join(curdir, "training")
            if not os.path.exists(dest):
                os.mkdir(dest)
        elif count == 14000:
            dest = os.path.join(curdir, "testing")
            if not os.path.exists(dest):
                os.mkdir(dest)
        count+=1
        destdir = os.path.join(dest,str(int(d[0])))
        if not os.path.exists(destdir):
            os.mkdir(destdir)
        img = d[1]
        filepath = unique_name(destdir)
        print('[^_^] Write image to %s' % filepath)
        if not filepath:
            continue
        sig = cv2.imwrite(filepath,img)
        if not sig:
            print('Error')
            exit(-1)


def unique_name(pardir,suffix='jpg'):
    filename = '{0}.{1}'.format(random.randint(1,10**8),suffix)
    filepath = os.path.join(pardir,filename)
    if not os.path.exists(filepath):
        return filepath
    unique_name(pardir,suffix)
    


if __name__ == '__main__':
#    filename = 'fer2013.csv'
#    filename = os.path.join(curdir,filename)
    gen_record(1)
    
    # ##################### test
    # tmp = unique_name('./Training','Training')
    # print(tmp)
