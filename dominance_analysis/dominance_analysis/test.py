import pandas as pd
from dominance_analysis import Dominance

data = pd.read_csv("data/Data_4_Variables.csv")
dominance = Dominance(data, "Y")

print("Incremental R Square : ")
print(dominance.incremental_rsquare())
print("Model R Square Stats : ")
print(dominance.model_stats())
