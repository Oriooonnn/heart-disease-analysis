# heart-disease-analysis
This program pefrorms an Exploratory Data Analysis on Kaggle Heart Disease dataset.
Main goal is to identify key rist factors such as age, gender and cholesterol and visualize them.
Achieved goals:
-Cleaned dataset from abnormal cholesterol values
-Visualized distribution of heart diseases cases
-Compared heart diseases occurrence between genders and age groups
-Calculated percentage of heart disease among people over 60 years old

Analisys include 
-Visualizations
-Data Cleaning
-Statistical insights


Python in data cleaning:
hearts_clean = hearts[(hearts["Cholesterol"] > 0) & (hearts["Cholesterol"] < 400)]
hearts["Cholesterol"] = hearts["Cholesterol"].replace(0,np.nan)
