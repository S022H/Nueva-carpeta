import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("peditos\\pedos.csv")

sns.lineplot(x="fecha",y="pedos",data=pd)
plt.show()
