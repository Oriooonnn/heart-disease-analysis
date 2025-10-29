from cProfile import label

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from IPython.core.pylabtools import figsize
from pandas.plotting import boxplot
#Otwarcie pliku csv
hearts = pd.read_csv('heart.csv')
#Wydrukowanie Pierwszych Pięciu
pierwsze = hearts.head()
ksztalt = hearts.shape
informacje = hearts.info
opisz = hearts.describe()
dane = hearts['HeartDisease'].value_counts()
kategorie = dane.index
liczby = dane.values
#Deklaracja nowego wykresu
plt.figure(figsize=(10,10))
#Wykres
plt.bar(kategorie, liczby)
#Podziałki na wykresie
plt.xticks([0,1],["Zdrowi","Chorzy"])
plt.xlabel("Status")
plt.ylabel("Ilość Badanych")
plt.title("Rozkład pacjentów z choroba serca")
plt.show()
plt.figure(figsize=(10,10))
#Deklaracja Histogramu
plt.hist(hearts['Age'], bins=10)
plt.xlabel("Wiek")
plt.ylabel("Ilość Badanych")
plt.show()
print(opisz)
print(informacje)
print(pierwsze)
print(ksztalt)
print(hearts.shape)
print(hearts.info())
hearts_clean = hearts[(hearts["Cholesterol"] > 0) & (hearts["Cholesterol"] < 400)]
print(hearts.describe())
(hearts['HeartDisease'].value_counts())
Chore_Kobiety = len(hearts[(hearts['Sex'] == "F") & (hearts['HeartDisease'] ==1) & (hearts['Age'] > 50)])
Chorzy_Mezczyzni = len(hearts[(hearts['Sex'] == "M") & (hearts["HeartDisease"] ==1) & (hearts['Age'] > 50)])
Dane = [Chore_Kobiety, Chorzy_Mezczyzni]
Plec = ["Kobieta", "Mezczyzna"]
plt.figure(figsize=(8,6))
plt.bar(Plec, Dane)
plt.xlabel("Płeć")
plt.ylabel("Ilość zachorowań")
plt.show()
plt.figure(figsize=(8,6))
Sredni_Cholestero = int(hearts['Cholesterol'].mean())
print(Sredni_Cholestero)
hearts.boxplot(column="HeartDisease",by="Cholesterol")
plt.xlabel("Zachorowania")
plt.ylabel("Cholesterol")
plt.show()
zdrowi = hearts_clean[hearts_clean["HeartDisease"] == 0]
chorzy = hearts_clean[hearts_clean["HeartDisease"] == 1]

plt.figure(figsize=(10,6))
plt.hist((zdrowi["Age"]),bins=15,alpha=0.6,color="green",label= "Zdrowi")
plt.hist((chorzy["Age"]),bins=15,alpha=0.6,color="red",label="Chorzy")
plt.xlabel("Wiek")
plt.ylabel("Liczba Pacjentów")
plt.legend()
plt.show()
po_60 = hearts[hearts["Age"] > 60]
chorzy_po_60 = po_60[po_60["HeartDisease"] == 1]
procent = (len(chorzy_po_60)/ len(po_60)) * 100
print(f"Osób po 60 {len(po_60)}")
print(f"W tym chorych {len(chorzy_po_60)}")
print(f"Co stanowi {procent} procent")
mezczyzni = hearts[hearts["Sex"] == "M"]
mezczyzni_chorzy = mezczyzni[mezczyzni["HeartDisease"] == 1]
kobiety = hearts[hearts["Sex"] == "F"]
kobiety_chore = kobiety[kobiety["HeartDisease"] == 1]
procent_m = (len(mezczyzni_chorzy) / len(mezczyzni)) * 100
procent_f = (len(kobiety_chore) / len(kobiety)) * 100
Plcie = ["Mezczyzni", "Kobiety"]
Procenty = [procent_m, procent_f]
plt.figure(figsize=(8,6))
plt.bar(Plcie,Procenty,color=["blue","red"],edgecolor="black")
plt.xlabel("Płeć")
plt.ylabel("Procenty")
plt.ylim(0,100)
plt.grid(axis= "y", alpha = 0.3)
plt.show()
plt.figure(figsize=(8,6))
plt.boxplot([zdrowi["Cholesterol"],chorzy["Cholesterol"]], labels=["Zdrowi","Chorzy"], patch_artist=True,boxprops=dict(facecolor="lightblue"),medianprops=dict(color="red",linewidth=2))
plt.xlabel("Wiek")
plt.ylabel("Cholesterol")
plt.title("Zależność cholesterolu wśród zdrowych i chorych")
plt.grid(axis="y", alpha =0.3)
plt.show()
hearts["Cholesterol"] = hearts["Cholesterol"].replace(0,np.nan)



print(f"Zdrowi {zdrowi["Cholesterol"].min()}")
print(f"Zdrowi {zdrowi["Cholesterol"].max()}")
print(f"Chorzy {chorzy["Cholesterol"].min()}")
print(f"Chorzy {chorzy["Cholesterol"].max()}")
Heart_Rate = hearts["MaxHR"]
Sredni_Heart_Rate = Heart_Rate.mean()
print(f"Średni Heart Rate wynosi {Sredni_Heart_Rate}")
