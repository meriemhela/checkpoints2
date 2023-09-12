# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:28:18 2023

@author: helali meriem
"""

#----------------- Preprocessing phase: ---------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\dell\Downloads\titanic-passengers.csv",delimiter=';')
df=pd.DataFrame(data)

#showing the head of the dataset
print("Head of the dataset:")
df.head()

# Get general information about the data columns and values
print("\nGeneral information about the dataset:")
print(df.info())

# Find missing values in the DataFrame
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

#replace missing with the appropriate values.
   #numerical values
df['Age'].fillna(df['Age'].mean(),inplace=True)
df

   #categorical values
#replace missing values in categorical columns(Cabin) with the mode (the most frequent category) 
df['Cabin'].fillna(df['Cabin'].mode()[0], inplace=True)
df

df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df

#----------------- Visualization phase ---------------------------------------
#studying the distribution of the most important features
#after studing the situation the most impotant features are : Survived , Age and Sex

plt.title("Histogram of diffrent ages")
plt.xlabel("Age")
df['Age'].plot.hist(color='blue')
plt.show()

plt.title("Barplot of Survived people")
plt.xlabel("Survived")
plt.ylabel("number of survived people")
vc =df['Survived'].value_counts()
vc.plot.bar(rot=45)
plt.show()

plt.title("Barplot of Sex")
plt.xlabel("Sex")
plt.ylabel("")
vc =df['Sex'].value_counts()
vc.plot.bar(rot=45)
plt.show()

#Visualize the correlation between Sex and Age
sns.violinplot(x='Sex', y='Age', hue='Survived', data=df, split=True)

plt.title("Correlation between Sex and Age with Survival")
plt.xlabel("Sex")
plt.ylabel("Age")
plt.legend(title='Survived', labels=['No', 'Yes'])

plt.show()

#Pick two other features and study their impact on the survival of the individuals.

#Have a look at this function:
def plot_correlation_map( df ):
    corr = df.corr()
    s , ax = plt.subplots( figsize =( 12 , 10 ) )
    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )
    s = sns.heatmap(
    corr,
    cmap = cmap,
    square=True,
    cbar_kws={ 'shrink' : .9 },
    ax=ax,
    annot = True,
    annot_kws = { 'fontsize' : 12 }
)








