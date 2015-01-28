from pandas import Series, DataFrame
import pandas as pd
import numpy as np

main_dir="/Users/Peizhi/Desktop/Duke 2015 SPRING/PUBPOL 590"
txt_file="/File1_small.txt"

A1=pd.read_csv(main_dir + txt_file,sep = " ")
A1[66:100]
A1[A1.kwh>30]

