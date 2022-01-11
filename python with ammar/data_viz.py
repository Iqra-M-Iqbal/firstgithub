import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
titanic=sns.load_dataset("titanic")
#print(titanic)
#x= sns.catplot(x="sex", y="survived", hue="embark_town", kind="bar", data=titanic)
#plt.show()
p= sns.catplot(x="sex", y="survived", hue="embark_town", kind="bar", data=titanic)
p.set_title("My first graph")
#p.set_title("Baba_aammar ka count plot for kashti")
plt.show()