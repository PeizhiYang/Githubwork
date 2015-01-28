from pandas import Series, DataFrame
import pandas as pd
import numpy as np

main_dir = "/Users/Peizhi/Desktop/Duke 2015 SPRING/PUBPOL 590"
csv_file = "/sample_data_clean.csv"
txt_file = "/sample_data_clean.txt"

df = pd.read_csv(main_dir+csv_file)
df2 = pd.read_table(main_dir+csv_file)

type(df)
consump = df.consump
df[5:10]
consump[5:10]
df.consump[5:10]

#==; !=; >=; <= 

#df is testing true or false if followed by conditions; df[df] is representing
df. panid==4
df[df.panid==4]
df[df.consump>2]

#test if the panid >2; could be concise if the panid is assigned to a shorcut
df.panid>2
#represent whole row
df[df.panid>2]
#only represent panid
df.panid[df.panid>2]
#df is the stuff represented
df.consump[df.panid>2]