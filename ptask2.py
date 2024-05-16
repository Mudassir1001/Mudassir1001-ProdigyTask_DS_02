import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample Titanic dataset
data = {
    'PassengerId': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Survived': [0, 1, 1, 1, 0, 0, 1, 0, 1, 0],
    'Pclass': [3, 1, 3, 1, 3, 3, 1, 3, 2, 3],
    'Name': [
        'Braund, Mr. Owen Harris', 'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
        'Heikkinen, Miss. Laina', 'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
        'Allen, Mr. William Henry', 'Moran, Mr. James',
        'McCarthy, Mr. Timothy J', 'Palsson, Master. Gosta Leonard',
        'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)', 'Nasser, Mrs. Nicholas (Adele Achem)'
    ],
    'Sex': ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'male', 'female', 'female'],
    'Age': [22, 38, 26, 35, 35, None, 54, 2, 27, 14],
    'Fare': [7.25, 71.2833, 7.925, 53.1, 8.05, 8.4583, 51.8625, 21.075, 11.1333, 30.0708],
    'Embarked': ['S', 'C', 'S', 'S', 'S', 'Q', 'S', 'S', 'S', None]
}

titanic = pd.DataFrame(data)

# Data Cleaning

# Fill missing Age values with the median
titanic['Age'].fillna(titanic['Age'].median(), inplace=True)

# Fill missing Embarked values with the mode
titanic['Embarked'].fillna(titanic['Embarked'].mode()[0], inplace=True)

# Convert 'Survived' and 'Pclass' to categorical types
titanic['Survived'] = titanic['Survived'].astype('category')
titanic['Pclass'] = titanic['Pclass'].astype('category')

# Drop duplicates if any
titanic.drop_duplicates(inplace=True)

# Exploratory Data Analysis (EDA)

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Plot the distribution of the Age
plt.figure(figsize=(10, 6))
sns.histplot(titanic['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Plot the count of survivors vs non-survivors
plt.figure(figsize=(8, 5))
sns.countplot(x='Survived', data=titanic)
plt.title('Survival Count')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()

# Plot survival rate by passenger class
plt.figure(figsize=(10, 6))
sns.countplot(x='Pclass', hue='Survived', data=titanic)
plt.title('Survival Count by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.show()

# Plot survival rate by sex
plt.figure(figsize=(10, 6))
sns.countplot(x='Sex', hue='Survived', data=titanic)
plt.title('Survival Count by Sex')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()

# Survival rate by Age
plt.figure(figsize=(10, 6))
sns.histplot(titanic[titanic['Survived'] == 1]['Age'], bins=30, kde=True, color='blue', label='Survived')
sns.histplot(titanic[titanic['Survived'] == 0]['Age'], bins=30, kde=True, color='red', label='Not Survived')
plt.title('Survival Rate by Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# Survival rate by Fare
plt.figure(figsize=(10, 6))
sns.histplot(titanic[titanic['Survived'] == 1]['Fare'], bins=30, kde=True, color='blue', label='Survived')
sns.histplot(titanic[titanic['Survived'] == 0]['Fare'], bins=30, kde=True, color='red', label='Not Survived')
plt.title('Survival Rate by Fare')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# Survival rate by Embarked
plt.figure(figsize=(10, 6))
sns.countplot(x='Embarked', hue='Survived', data=titanic)
plt.title('Survival Rate by Embarked')
plt.xlabel('Port of Embarkation')
plt.ylabel('Count')
plt.show()
