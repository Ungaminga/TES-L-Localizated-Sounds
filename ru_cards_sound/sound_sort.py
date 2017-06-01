#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 00:20:31 2017

@author: loljkpro
"""
import os, sys, re, shutil
  
def process_exceptions(F):
    if (re.search(r'deshaan_avenger_deshaan_sneak', F)):
        os.makedirs('deshaan_avenger', exist_ok=True)
        os.makedirs('deshaan_sneak', exist_ok=True)
        shutil.copy(F, os.path.join('deshaan_avenger', F.replace('_deshaan_sneak', '')))
        shutil.move(F, os.path.join('deshaan_sneak', F.replace('deshaan_avenger_', '')))
        return True
    return False

# load directory name
dir = os.getcwd()
if len(sys.argv) >= 2:
    dir = (sys.argv[1])
for F in os.listdir(dir):
    s = re.search(r'.wav', F)
    if s:
        # deshaan_avenger_deshaan_sneak is exception of main rule of names
        if process_exceptions(F):
            continue;
        # taking name left of.wav or _(some names extansion)          and exclude .wav from filename  
        subdir = re.split(r'(.wav|(_(attack.*|enter_play.*|trigger|rewind|last_gasp|reward|hit|pilfer).wav))', F)[0]
        # mkdir has no exist_ok and throw exception
        os.makedirs(subdir, exist_ok=True)
        try:
            shutil.move(F, subdir)
        except OSError:
            os.remove(F)