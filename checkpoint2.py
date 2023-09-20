#                                 . Preprocessing phase.


#importing the dataset : 
import pandas as pd
data = pd.read_csv(r"C:\Users\dell\Downloads\titanic-passengers.csv",delimiter=';')
df=pd.DataFrame(data)

#showing the head of the dataset:
print("Head of the dataset:")
print()
print(df.head())
print("*********************************************************************")

# Get general information about the data columns and values:
print("\nGeneral information about the dataset:")
print()
print(df.info())

print("*********************************************************************")

# Find missing values in the DataFrame:
missing_values = df.isnull().sum()
print("Missing values in each column:")
print()
print(missing_values)

print("*********************************************************************")

#replace missing with the appropriate values:
   #numerical values: 
print("replace missing with the appropriate values :")
print()
df['Age'].fillna(df['Age'].mean(),inplace=True)
print(df)
print("*********************************************************************")

   #categorical values:
#replace missing values in categorical columns(Cabin) with the mode (the most frequent category) 
print("replace missing values in categorical columns(Cabin) with the mode :")
print()
df['Cabin'].fillna(df['Cabin'].mode()[0], inplace=True)
print(df['Cabin'])


print()
print()

print("replace missing values in categorical columns(Embarked) with the mode :")
print()
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
print(df['Embarked'])

print("*********************************************************************")

#confirm that we don't have missing values:
print("confirm that we don't have missing values:")
print()
missing_values = df.isnull().sum()
print(missing_values)



#                                 . Visualization phase .

import matplotlib.pyplot as plt
from matplotlib.pyplot import style
import seaborn as sns

print("studying the distribution of age and sex :")
style.use('ggplot')
color=['royalblue']
plt.bar(df['Sex'],df['Age'], color=color,width=0.5)
plt.xlabel("sex")
plt.ylabel("Age")
plt.title(' study the distribution of sex in relation to age')
plt.show()

print('Visualize the correlation between Sex and Age:')
correlation = sns.FacetGrid(df,col='Sex')
correlation.map(plt.hist,'Age',bins=20)
print()
print("we can observe that the largest number of passengers on the Titanic are men, especially between [0 - 60] years old. And between [60 - 80] we can say that there are not many women at this age ")

print("Pick two other features and study their impact on the survival of the individuals")
print('Visualize the correlation between Sex and Age:')
correlation = sns.FacetGrid(df,col='Survived')
correlation.map(plt.hist,'Cabin')
print()


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







