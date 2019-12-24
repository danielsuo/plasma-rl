###########################################################################
##
##This file loads sample data from DIII-D experiment
##
##Data from 10 DIII-D plasma experiments(shots) are saved in 'shot_data.npz',including ones plotted in the 
##2019 NATURE paper in FIG2 (a)-148778 and (c)-159593.
##Each experiment is indexed by a six digit shot number.
##In the loaded dictionary, the keys are shot number.
##Each shot is also save as dictionary, with keys:'is_disruptive','disruption_time',and 'X'
##'is_disruptive' indicates whether this shot has a disruption.
##'disruption' time is the time for disruption (miliseconds), which is always t_total-30 in this pre-processed and normalized database . 
##
##'X' is the 'features' for each shot, save as an array with shape (num_time_steps,num_features)
##In this database, num_features=142. index 0-15 correspond to 16 0-D scalar signals, such as the plasma current,and index 16-142 correspond to two 1-D profile signals (length 64 each).
##num_time_steps can vary from 1000-10000
##For each shot, at each time step, a model should be able to output a 'disruption score' to indicate whether a disruption is coming in 30 time steps, without seeing any 'future' information. 
##The labels, or y can be any target funtion defined depending on the disruptivity of the shot. 
############################################################################
import numpy as np

d=np.load('shot_data.npz',allow_pickle=True)
shot_data=d['shot_data'].item()


print('shot_number,X.shape,is_disruptive','disption_time')
for k in shot_data.keys():
  print(k,shot_data[k]['X'].shape,shot_data[k]['is_disruptive'],shot_data[k]['disruption_time'])


