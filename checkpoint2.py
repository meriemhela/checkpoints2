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

data['Sex'].value_counts().plot(kind="pie", autopct="%.2f")
plt.show()
print("we can observe that the largest number of passengers on the Titanic are men")


sns.displot(data['Age'])
plt.title("Age distribution :")
plt.show()
print("we can observe that the largest number of passengers on the Titanic are young people (between 20-40)")

print("*********************************************************************")
print()

print('Visualize the correlation between Sex and Age:')
sns.countplot(x='Survived',hue ='Sex',data=df)
plt.show()
print("we can observe that the largest number of female survivors on the Titanic then male ")

titanic=sns.FacetGrid(df,col="Survived")
titanic.map(plt.hist,"Age",bins=10)
plt.show()
print()
print("we can observe that the largest number of young passengers on the Titanic are not survived ")



print()
print("*********************************************************************")
cleanup={"Survived":{"yes":1,"no":0}}
df.replace(cleanup,inplace=True)
print(df[["Pclass","Survived"]].groupby(["Pclass"],as_index=True).mean())

print()
print("*********************************************************************")
# Drop the 'Names' column
df = df.drop(columns=['Name'])

# Print the resulting DataFrame
print(df)


print()
print("*********************************************************************")
Title_Dictionary = {
    "Capt": "Officer",
    "Col": "Officer",
    "Major": "Officer",
    "Dr": "Officer",
    "Rev": "Officer",
    "Jonkheer": "Royalty",
    "Don": "Royalty",
    "Sir": "Royalty",
    "Lady": "Royalty",
    "theCountess": "Royalty",
    "Dona": "Royalty",
    "Mme": "Miss",
    "Mlle": "Miss",
    "Miss": "Miss",
    "Ms": "Mrs",
    "Mr": "Mrs",
    "Mrs": "Mrs",  
    "Master": "Master"
}







