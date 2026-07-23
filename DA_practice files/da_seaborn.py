

##!pip install seaborn
import seaborn as sns
##seaborn.__version__

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
dataset = pd.read_csv('data.csv')

"""###1_Statistical Relationship - Scatter Plot"""

sns.relplot(x='hours',y='marks',hue='age',data=dataset)
plt.plot()
"""###1_Statistical Relationship - Line Plot"""

sns.relplot(x='hours',y='marks',hue='age',data=dataset,kind="line",style="internet")

"""###1_Statistical Relationship - Multiple"""

sns.relplot(x='hours',y='marks',hue='age',data=dataset,col="internet")

"""###2_Data Distribution - Histogram"""

sns.displot(dataset, x="age", binwidth=0.5, hue="internet")
sns.displot(dataset, x="age", bins = [10,11,12,13,14,15,16,17,18,19,20])
plt.show()
"""###2_Data Distribution - Multiple"""

sns.displot(dataset, x="marks", col="internet")
"""###2_Data Distribution - Bivariate distributions"""

sns.displot(dataset, x="age", y="marks",hue="internet")

"""###2_Data Distribution - Kernel Density Estimation"""

sns.displot(dataset, x="age", y="marks",kind="kde",hue="internet")

"""###2_Data Distribution - Pair Plot

"""

sns.pairplot(dataset)

"""###3_Categorical Data - Scatterplot"""

sns.catplot(x="age", y="marks", data=dataset, hue="internet")

"""###3_Categorical Data - Box Plot

"""

sns.catplot(x="age", y="marks", kind="box", data=dataset, hue="internet")

"""###Regression Output"""

sns.regplot(x="marks", y="hours", data=dataset);

sns.lmplot(x="marks", y="hours", data=dataset,hue="internet",markers=["o", "x"], palette="Set1");

"""### Using SNS theme in other graph"""

import numpy as np
import matplotlib.pyplot as plt
def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 10):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
sns.set_context("paper") #talk/poster/paper
sinplot()
