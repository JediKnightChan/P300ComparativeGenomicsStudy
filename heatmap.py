# import sys
# sys.path.append("/home/jediknight/.local/lib/python3.8/site-packages")

import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(20,12))

df = pd.read_csv("final.tsv", sep="\t", index_col=0)
sns.heatmap(df, annot=True)

plt.savefig("heatmap.png", dpi=300)
