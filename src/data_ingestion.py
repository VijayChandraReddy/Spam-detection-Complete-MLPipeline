import pandas as pd
import os
from sklearn.model_selection import train_test_split
import logging

#Ensure log directory exists
log_dir = 'logs'
os.mkdir(log_dir,exist_ok = True)

