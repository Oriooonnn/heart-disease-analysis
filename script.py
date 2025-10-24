import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import boxplot

hearts = pd.read_csv('heart.csv')
#pierwsze = hearts.head()
#ksztalt = hearts.shape
#informacje = hearts.info
opisz = hearts.describe()
dane = hearts['HeartDisease'].value_counts()
kategorie = dane.index
liczby = dane.values
#plt.figure(figsize=(10,10))
#plt.bar(kategorie, liczby)
#plt.xticks([0,1],["Zdrowi","Chorzy"])
#plt.xlabel("Status")
#plt.ylabel("Ilość Badanych")
#plt.title("Rozkład pacjentów z choroba serca")
#plt.show()
#plt.figure(figsize=(10,10))
#plt.hist(hearts['Age'], bins=10)
#plt.xlabel("Wiek")
#plt.ylabel("Ilość Badanych")
#plt.show()
#print(opisz)
#print(informacje)
#print(pierwsze)
#print(ksztalt)
#print(hearts.shape)
#print(hearts.info())
#print(hearts.describe())
#(hearts['HeartDisease'].value_counts())
#Chore_Kobiety = len(hearts[(hearts['Sex'] == "F") & (hearts['HeartDisease'] ==1) & (hearts['Age'] > 50)])
#Chorzy_Mezczyzni = len(hearts[(hearts['Sex'] == "M") & (hearts["HeartDisease"] ==1) & (hearts['Age'] > 50)])
#Dane = [Chore_Kobiety, Chorzy_Mezczyzni]
#Plec = ["Kobieta", "Mezczyzna"]
#plt.figure(figsize=(8,6))
#plt.bar(Plec, Dane)
#plt.xlabel("Płeć")
#plt.ylabel("Ilość zachorowań")
#plt.show()
plt.figure(figsize=(8,6))
Sredni_Cholestero = int(hearts['Cholesterol'].mean())
print(Sredni_Cholestero)
hearts.boxplot(column="HeartDisease",by="Cholesterol")
plt.xlabel("Zachorowania")
plt.ylabel("Cholesterol")
plt.show()
