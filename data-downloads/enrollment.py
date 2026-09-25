import pandas as pd

data = pd.read_csv("CRDC2013_14.csv", encoding = "Latin-1")


data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]

all_enrollment = data["total_enrollment"].sum()

for i in data.columns:
    data[i] = pd.to_numeric(data[i], errors = "coerce")
    data[i] = data[i] / all_enrollment
    
print(data[i])
