import pandas as pd
import read

d = read.load_data()

domains = d["url"]
domains = domains[:99:]

for name, row in domains.items():
    print("{0}: {1}".format(name, row))