
# coding: utf-8

# In[58]:


import csv
x = open("guns.csv", "r")
y = csv.reader(x)
data = list(y)
headers = data[1:]



# In[59]:


years = []
for column in headers:
    second_column = column[1]
    years.append(second_column)
    
year_counts = {}
for i in years:
    if i not in year_counts:
        year_counts[i] = 1
    else:
        year_counts[i] = year_counts[i] + 1
        
print(year_counts)
    
    


# In[60]:


import datetime

dates = {}
for column in headers:
    year = int(column[1])
    month = int(column[2])
    w = datetime.datetime(year, month, day = 1)
    if w in dates:
        dates[w] = dates[w] + 1
    else:
        dates[w] = 1
    date_counts = dates
date_counts
        


# In[61]:


#sex column counts
sex_counts = {}
for item in headers:
    sex = item[5]
    if sex not in sex_counts:
        sex_counts[sex] = 0
    else:
        sex_counts[sex] = sex_counts[sex] + 1
sex_counts


# In[62]:


#race column counts
race_counts = {}
for item in headers:
    race = item[7]
    if race not in race_counts:
        race_counts[race] = 0
    else:
        race_counts[race] = race_counts[race] + 1
race_counts


# In[ ]:


# It appears the counts for white people outnumber all other races whilst that of Native Americans are pretty low.
# The count for Black people outnumber that of hispanics more than twice the amount


# In[63]:


import csv

cens = open("census.csv", "r")
census = list(csv.reader(cens))
census


# In[64]:


mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Black": 40250635,
    "Hispanic": 44618105,
    "Native American/Native Alaskan": 3739506,
    "White": 197318956
}



race_per_hundredk = {}
for key, m in race_counts.items():
    race_per_hundredk[key] = (m/mapping[key])*100000
    
race_per_hundredk


# In[66]:


intents = [i[3] for i in data]
races = [i[8] for i in data]

homicide_race_counts = dict()
for i, race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i] == "Homicide":
        homicide_race_counts[race] = homicide_race_counts[race] + 1
 


race_per_hundredk = {}
for key, m in homicide_race_counts.items():
    race_per_hundredk[key] = (m / mapping[key])*100000
    
race_per_hundredk

