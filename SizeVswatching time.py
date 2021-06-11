import csv
from typing import Dict, Sized
from numpy.lib import corrcoef
import plotly.express as px
import numpy as np

def getdataSource(data_source):
    avg_time=[]
    size=[]
    with open(data_source) as f:
        df=csv.DictReader(f)
        for i in df:
            avg_time.append(float(i["	Average time spent watching TV in a week (hours)"]))
            size.append(float(i["Size of TV"]))

    return {"x":avg_time,"y":size}

def findCorrelation(data):
    correlation=np.corrcoef(data["x"],data["y"])
    print("correlation between size of tv and avrage watching hours:",correlation[0,1])

def setup():
    data=getdataSource("pro 106/Size of TV,_Average time spent watching TV in a week (hours).csv")
    findCorrelation(data)

setup()