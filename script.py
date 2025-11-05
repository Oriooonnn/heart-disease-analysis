"""
Heart Disease Data Analysis
===========================
Dataset: Kaggle Heart Disease Dataset
Goal: Exploratory Data Analysis to identify risk factors
Author: Jan Kuśnierz
Date:29.10.2025

Analysis Includes:
-Data Cleaning
-Visualization (Histograms, Barcharts, Boxplot)
-Key findings (Age,Gender,Cholesterol)
"""



#=========IMPORTS==============
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


hearts = pd.read_csv('heart.csv')
first = hearts.head()
shape = hearts.shape
information = hearts.info
description = hearts.describe()
data = hearts['HeartDisease'].value_counts()
category = data.index
numbers = data.values
plt.figure(figsize=(10,10))
plt.bar(category, numbers)
plt.xticks([0,1],["Heart disease","No Heart disease"])
plt.xlabel("Status")
plt.ylabel("Amount of patients")
plt.title("Distribution of patients with heart disease")
plt.show()
plt.figure(figsize=(10,10))
plt.hist(hearts['Age'], bins=10)
plt.xlabel("Age")
plt.ylabel("Amount of patients")
plt.show()
print(description)
print(information)
print(first)
print(shape)
print(hearts.shape)
print(hearts.info())
#Cleaning Data from Hearts.csv(Abstract cholesterol numbers)
hearts_clean = hearts[(hearts["Cholesterol"] > 0) & (hearts["Cholesterol"] < 400)]
print(hearts.describe())
(hearts['HeartDisease'].value_counts())
Disease_Women = len(hearts[(hearts['Sex'] == "F") & (hearts['HeartDisease'] ==1) & (hearts['Age'] > 50)])
Disease_Men = len(hearts[(hearts['Sex'] == "M") & (hearts["HeartDisease"] ==1) & (hearts['Age'] > 50)])
Sex_Data = [Disease_Women, Disease_Men]
Sex = ["Woman", "Man"]
plt.figure(figsize=(8,6))
#Bar chart: Difference between men and women with heart diseases
plt.bar(Sex, Sex_Data)
plt.xlabel("Sex")
plt.ylabel("Amount of diseases")
plt.show()
plt.figure(figsize=(8,6))
Average_Cholesterol = int(hearts['Cholesterol'].mean())
print(Average_Cholesterol)
no_heart_disease = hearts_clean[hearts_clean["HeartDisease"] == 0]
heart_disease = hearts_clean[hearts_clean["HeartDisease"] == 1]

plt.figure(figsize=(10,6))
#Histogram: Age and heart diseases
plt.hist((no_heart_disease["Age"]),bins=15,alpha=0.6,color="green",label= "Zdrowi")
plt.hist((heart_disease["Age"]),bins=15,alpha=0.6,color="red",label="Chorzy")
plt.xlabel("Age")
plt.ylabel("Amount of patients")
plt.legend()
plt.show()
#What percentage of people over 60 has a heart disease?
after_60 = hearts[hearts["Age"] > 60]
disease_after_60 = after_60[after_60["HeartDisease"] == 1]
percentage = (len(disease_after_60)/ len(after_60)) * 100
print(f"People over 60 {len(after_60)}")
print(f"People over 60 who have disease {len(disease_after_60)}")
print(f"Which is  {percentage} %")
Man = hearts[hearts["Sex"] == "M"]
Man_Heart_Disease = Man[Man["HeartDisease"] == 1]
Woman = hearts[hearts["Sex"] == "F"]
Woman_Heart_Disease = Woman[Woman["HeartDisease"] == 1]
percentage_m = (len(Man_Heart_Disease) / len(Man)) * 100
percentage_f = (len(Woman_Heart_Disease) / len(Woman)) * 100
Sex2 = ["Men", "Women"]
Percentages = [percentage_m, percentage_f]
plt.figure(figsize=(8,6))
#Comparision of Men and women in case of heart diseases with percentages
plt.bar(Sex2,Percentages,color=["blue","red"],edgecolor="black")
plt.xlabel("Sex")
plt.ylabel("Percentage")
plt.ylim(0,100)
plt.grid(axis= "y", alpha = 0.3)
plt.show()
plt.figure(figsize=(8,6))
#Boxplot: Does cholesterol really matter in case of heart diseases?
plt.boxplot([no_heart_disease["Cholesterol"],heart_disease["Cholesterol"]], labels=["Heart Disease","No Heart Disease"], patch_artist=True,boxprops=dict(facecolor="lightblue"),medianprops=dict(color="red",linewidth=2))
plt.xlabel("Age")
plt.ylabel("Cholesterol")
plt.title("Cholesterol among people with heart disease and without heart disease")
plt.grid(axis="y", alpha =0.3)
plt.show()
hearts["Cholesterol"] = hearts["Cholesterol"].replace(0,np.nan)



print(f"Without Heart Disease {no_heart_disease["Cholesterol"].min()}")
print(f"Without Heart Disease {heart_disease["Cholesterol"].max()}")
print(f"Heart Disease {no_heart_disease["Cholesterol"].min()}")
print(f"Heart Disease {heart_disease["Cholesterol"].max()}")
#Heart Rate in progress
Heart_Rate = hearts["MaxHR"]
Average_Heart_Rate = Heart_Rate.mean()
print(f"Average Heart Rate is {Average_Heart_Rate}")
