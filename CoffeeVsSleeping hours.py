import csv
from typing import Dict
from numpy.lib import corrcoef
import plotly.express as px
import numpy as np

def getdataSource(data_source):
    coffee_cup=[]
    sleep_hours=[]
    with open(data_source) as f:
        df=csv.DictReader(f)
        for i in df:
            coffee_cup.append(float(i["Coffee in ml"]))
            sleep_hours.append(float(i["sleep in hours"]))

    return {"x":coffee_cup,"y":sleep_hours}

def findCorrelation(data):
    correlation=np.corrcoef(data["x"],data["y"])
    print("correlation between cups of coffee and sleepig hours:",correlation[0,1])

def setup():
    data=getdataSource("pro 106/cups of coffee vs hours of sleep.csv")
    findCorrelation(data)

setup()