# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-

#%%
import soundfile
import os
from glob import glob

cwd = os.getcwd()
cur_path_name = os.path.split(cwd)[-1]
out_path = os.path.join(cwd, f'{cur_path_name}_output')
if (not os.path.isdir(out_path)):
    os.mkdir(out_path)

wav_files = glob(os.path.join(cwd, '*.wav'))
for file in wav_files:
    data, samplerate = soundfile.read(file)
    new_file = os.path.join(out_path, os.path.split(file)[-1])
    soundfile.write(new_file, data, samplerate, subtype = 'PCM_16')
