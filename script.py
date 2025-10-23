import pandas as pd
import matplotlib.pyplot as plt
hearts = pd.read_csv('heart.csv')
pierwsze = hearts.head()
ksztalt = hearts.shape
informacje = hearts.info
opisz = hearts.describe()
dane = hearts['HeartDisease'].value_counts()
kategorie = dane.index
liczby = dane.values
plt.bar(kategorie, liczby)
plt.xticks([0,1],["Zdrowi","Chorzy"])
plt.xlabel("Status")
plt.ylabel("Ilość Badanych")
plt.title("Rozkład pacjentów z choroba serca")
plt.show()
#print(opisz)
#print(informacje)
#print(pierwsze)
#print(ksztalt)
#print(hearts.shape)
#print(hearts.info())
#print(hearts.describe())
#(hearts['HeartDisease'].value_counts())
