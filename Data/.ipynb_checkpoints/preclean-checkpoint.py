import pandas as pd
from datascience import *

bus = pd.read_csv('Data/bus.csv') # reads the csv file and loads it
ins = pd.read_csv('Data/ins.csv')
numlst = ins['iid'].str.split("_")
ins["bid"] = numlst.str[0].astype(int)
ins['timestamp'] = pd.to_datetime(ins['date'])
ins = ins[ins["score"] > 0]
ins = ins.rename(columns={"bid": "business id column"})
ins = ins.drop(columns = ['iid'])
bus_data = pd.merge(left = ins, right = bus,
                  left_on = "business id column", right_on = "business id column")
