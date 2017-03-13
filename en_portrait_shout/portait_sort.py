#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 00:20:31 2017

@author: loljkpro
"""
import os, sys, re, shutil

# load directory name
dir = os.getcwd()
if len(sys.argv) >= 2:
    dir = (sys.argv[1])
for F in os.listdir(dir):
    s = re.search(r'.wav', F)
    if s:
        subdir = re.split(r'_(fe|)male_', F)[0]
        # mkdir has no exist_ok and throw exception
        os.makedirs(subdir, exist_ok=True)
        shutil.move(F, subdir)