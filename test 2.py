from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/Peizhi/Desktop/Duke 2015 SPRING/PUBPOL 590"
git_dir = "/Users/Peizhi/Desktop/Duke 2015 SPRING/Githubwork"
csv_file = "sample_data_clean.csv"
#csv_file_bad = "/sample_data_clean.csv"
#df = pd.read_csv(main_dir + csv_file_bad) not always work the other one is always working

df = pd.read_csv(os.path.join(main_dir, csv_file))

#Python dta types
#strings

str1 = "hello, computer"
str2 = 'hello, human'
str3 = u'eep'

type(str1) #type str
type(str2) #type str
type(str3) #type str

## numeric
in1 = 10
float1 = 20.56
long1 = 99999999999999

## logical
bool1 = True
notbool1 = 0
bool2 = bool(notbool1) ## ????

## Creating LISTS AND TUPLES
## IN BRIEF, LISTS CAN BE CANGED, TUPLES CANNOT 
## WE ALMOST EXLUSIVELY USE LISTS

list1 = []
list1 
list2 = [7,8,'a']
list2[2] #output of this is 'a'
list2[2] = 5
#index starts from 0

## tuples, cant change
tup1 = (8,3,19)
tup1[2] #output is 19
tup1[2]=5 #does not accept assignment

##convert
list2 = list(tup1)
tup2 = tuple(list1)

##list can be append and extend
list2 = [8,3,19]
list2. append( [3,90] )
list2 = [8,3,90]
list2.extend([6,88])
len(list2)

##convert lists to series and dataframe
list4 = range (5,10) ## range(n,m) givea list from n to m-1

list5 = range(5) ##gives from 0 to m-1

##lists to series, case sensitive!!!
s1 = Series(list4)
s2 = Series(list5)

##lists/ series to dataframe
list6 = range(60,65)
zip(list4, list5)
zip(list4, list5, list6)
##bracket and ????????[] & ()?????????????????????????????????????????????????

zip1 = zip(list4, list5, list6)
df1 = DataFrame(zip1)
df1[0]
df1
df2 = DataFrame(zip1, columns = ['two', 'apple', 'smily face'])  ##column names
df3 = DataFrame(zip1, columns = [2, 'apple', 'smily face']) ###df3[2], df3['2"] keys????????

df3 [3:4] #slice out the row 3
df3[['apple', 'smily face']][3:4]## get column apple and smily face-- two brackets!!!

## make dataframe using dict notation---- renaming 
df4 = DataFrame({':(':list4, 9:list6}) #comma keep adding, but list should be the same length
dict1 = {':(':list4, 9:list6}
dict1[':(']

## how to stack series into another series
s1 = Series (list4)
s2 = Series(list6)