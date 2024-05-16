**Dataset**

The dataset is a simplified version of the Titanic dataset and includes the following columns:
PassengerId: Unique identifier for each passenger.
Survived: Survival status (0 = No, 1 = Yes).
Pclass: Passenger class (1 = 1st, 2 = 2nd, 3 = 3rd).
Name: Name of the passenger.
Sex: Sex of the passenger.
Age: Age of the passenger.
Fare: Fare paid by the passenger.
Embarked: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).
Analysis Steps
The eda_titanic.py script performs the following steps:

**Data Cleaning:**

Fill missing Age values with the median age.
Fill missing Embarked values with the mode.
Convert Survived and Pclass to categorical types.
Drop duplicate rows, if any.

**Exploratory Data Analysis (EDA):**

Plot the distribution of the Age column.
Plot the count of survivors vs. non-survivors.
Plot survival count by passenger class.
Plot survival count by sex.
Analyze survival rate by age.
Analyze survival rate by fare.
Analyze survival rate by port of embarkation.

**Visualizations:**

The script generates several visualizations to help understand the data, including histograms and count plots. These visualizations provide insights into the distribution of ages, survival rates by class, sex, fare, and embarkation port.
