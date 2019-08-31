# -*- coding: utf-8 -*-
"""

@author: Nashrah
"""

import pandas as pd

monthly_death=pd.read_csv('monthly_deaths.csv')
monthly_death['Year']=[d.split('-')[0] for d in monthly_death['date']]
#print(type(monthly_death['deaths']))


sum_deaths1841=0    
sum_births1841=0
year1841=monthly_death.loc[monthly_death["Year"]=="1841"]
for i in year1841["deaths"]:
    global sum_deaths1841
    sum_deaths1841+=i
for i in year1841["births"]:
    global sum_births1841
    sum_births1841+=i


sum_deaths1842=0    
sum_births1842=0    
year1842=monthly_death.loc[monthly_death["Year"]=="1842"]
for i in year1842["deaths"]:
    global sum_deaths1842
    sum_deaths1842+=i
for i in year1842["births"]:
    global sum_births1842
    sum_births1842+=i

sum_deaths1843=0    
sum_births1843=0
year1843=monthly_death.loc[monthly_death["Year"]=="1843"]
for i in year1843["deaths"]:
    global sum_deaths1843
    sum_deaths1843+=i
for i in year1843["births"]:
    global sum_births1843
    sum_births1843+=i


sum_deaths1844=0    
sum_births1844=0
year1844=monthly_death.loc[monthly_death["Year"]=="1844"]
for i in year1844["deaths"]:
    global sum_deaths1844
    sum_deaths1844+=i
for i in year1844["births"]:
    global sum_births1844
    sum_births1844+=i

sum_deaths1845=0    
sum_births1845=0
year1845=monthly_death.loc[monthly_death["Year"]=="1845"]
for i in year1845["deaths"]:
    global sum_deaths1845
    sum_deaths1845+=i
for i in year1845["births"]:
    global sum_births1845
    sum_births1845+=i

sum_deaths1846=0    
sum_births1846=0
year1846=monthly_death.loc[monthly_death["Year"]=="1846"]
for i in year1846["deaths"]:
    global sum_deaths1846
    sum_deaths1846+=i
for i in year1846["births"]:
    global sum_births1846
    sum_births1846+=i

sum_deaths1847=0    
sum_births1847=0
year1847=monthly_death.loc[monthly_death["Year"]=="1847"]
for i in year1847["deaths"]:
    global sum_deaths1847
    sum_deaths1847+=i
for i in year1847["births"]:
    global sum_births1847
    sum_births1847+=i

sum_deaths1848=0    
sum_births1848=0
year1848=monthly_death.loc[monthly_death["Year"]=="1848"]
for i in year1848["deaths"]:
    global sum_deaths1848
    sum_deaths1848+=i
for i in year1848["births"]:
    global sum_births1848
    sum_births1848+=i

sum_deaths1849=0    
sum_births1849=0
year1849=monthly_death.loc[monthly_death["Year"]=="1849"]
for i in year1849["deaths"]:
    global sum_deaths1849
    sum_deaths1849+=i
for i in year1849["births"]:
    global sum_births1849
    sum_births1849+=i
    
col_names=["Year","Births","Deaths"]

dataframe=[(1841,sum_births1841,sum_deaths1841),
           (1842,sum_births1842,sum_deaths1842),
           (1843,sum_births1843,sum_deaths1843),
           (1844,sum_births1844,sum_deaths1844),
           (1845,sum_births1845,sum_deaths1845),
           (1846,sum_births1846,sum_deaths1846),
           (1847,sum_births1847,sum_deaths1847),
           (1848,sum_births1848,sum_deaths1848),
           (1849,sum_births1849,sum_deaths1849)] 
    
new_df=pd.DataFrame(dataframe,columns=col_names)

new_df["Proportiona_deaths"]=new_df["Deaths"]/new_df["Births"]

import matplotlib.pyplot as plt
plt.plot(new_df["Year"],new_df["Proportiona_deaths"])
plt.scatter(new_df["Year"],new_df["Proportiona_deaths"])
plt.ylabel("proportions_death")
plt.xlabel("No of years")
plt.title("Decrease in proportions_death")






