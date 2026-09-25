import pandas as pd
import read
import datetime
import dateutil as dt


z = read.load_data()

def season(x):
    
    y = dt.parser.parse(x)
    return y.hour

z["hour"] = z["submission_time"].apply(season)

print(z["hour"].value_counts().head())