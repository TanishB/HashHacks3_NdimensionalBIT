from __future__ import print_function
import librosa
import numpy as np
import os
import pandas as pd
feature = []

def get_features(file):

	X, sample_rate = librosa.load(file , res_type='kaiser_fast') 
	mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=128).T,axis=0) 
	feature.append(list(mfccs))
	a = np.array(feature)
	return a
