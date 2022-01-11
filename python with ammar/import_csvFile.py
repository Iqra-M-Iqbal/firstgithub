import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pt
from seaborn.utils import get_dataset_names


chilla= pd.read_csv("data_viz.csv")
#print(chilla)
sns.set_theme(style= "ticks", color_codes=True)
a=sns.countplot(x="Gender", data=chilla, hue="Age")
a.set_title("My first count plot")
pt.show()
#sns.catplot(x="", y="", hue="Duration", kind= "bar" , data=chilla)
i=sns.catplot(x="Gender", y="Age", hue="Location",  kind="swarm", data=chilla)
i.fig.suptitle("My categorical plot")
pt.show()
#print(get_dataset_names())
