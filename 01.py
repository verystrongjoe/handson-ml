import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn

# load the data
oecd_bli =  pd.read_csv("datasets/lifesat/oecd_bli_2015.csv", thousands=",")
gdp_per_capita = pd.read_csv("datasets/lifesat/gdp_per_capita.csv", thousands=",", delimiter="\t", encoding='latin1', na_values="n/a")


print(oecd_bli)

#oecd_bli = oecd_bli[oecd_bli["I"]]
oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]
oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")

# prepare the data
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
X = np.c_
