import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns", 50)
pd.set_option('display.max_rows', 500)

survey_file_input = "survey.csv" 
d1 = pd.read_csv(survey_file_input)
print(d1)
d2 = d1 [["Age", "Gender", "Country", "state","self_employed","care_options", "remote_work","benefits", "tech_company","family_history", "treatment", "mental_health_consequence","phys_health_consequence"]]
print (d2)

d2.loc[(d2['benefits']).isin((['Yes', "Don't know"])), "benefits"] = "Yes"
d2.loc[(d2['care_options'].isin(['Yes', 'Not sure'])), "care_options"] = "Yes"

GF = ["female", "Cis Female", "F", "Woman", "4"] 
GM = ["W", "male", "e", "Male-ish", "maile", "Cis Male", "Mal", "Male (CIS)"]
LGBT = ["Trans-female", "something kinda male?", "queer/she/they 'non-binary"]

d2.loc[(d2['Gender'].isin(GF)), "Gender"] = "Female"
d2.loc[(d2['Gender'].isin(GM)), "Gender"] = "male"
d2.loc[(d2['Gender'].isin(LGBT)), "Gender"] = "nonbinary"

print(d2['Gender'].unique())

plt.figure(figsize = (10,5))
plt.subplot(1,2,1)

sns.countplot(d2['treatment'], palette = 'rocket')
plt.title('People who are taking treatment', fontsize=7)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.legend(fontsize=7)

plt.subplot(1,2,2)
sns.countplot(d2['tech_company'], hue = d2['treatment'], palette = 'rocket')
plt.title('People working in tech company taking treatment',  fontsize=7)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.legend(fontsize=7)
plt.show()
