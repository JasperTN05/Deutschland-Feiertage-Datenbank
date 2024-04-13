import requests
import pandas as pd

# Vorbereitung für API-Anfrage
states = ["NATIONAL","BW","BY","BE","BB","HB","HH","HE","MV","NI","NW","RP","SL","SN","ST","SH","TH"] # Liste aller Bundesländer
years = [str(1999 + i) for i in range(1, 32)] # Auflistung Jahre 2000 - 2030

# Abfrage nach Muster: Je Staat werden alle Jahre nacheinander abgefragt und zwischengespeichert
# Am Ende werden dann alle zwischengespeicherte DataFrames zusammengeführt.
full_data = []
for s in states:
  states_data = []
  for y in years:
    r = requests.get(f"https://feiertage-api.de/api/?jahr={y}&nur_land={s}")
    data = r.json()
    df_new = pd.DataFrame.from_dict(data, orient='index').reset_index() 
    df_new.columns = ['Feiertag', 'Datum', 'Hinweis']
    df_new[s] = 1
    states_data.append(df_new) # Hier wird immer ein DataFrame mit Informationen eines Jahr für ein Bundesland hinzugefügt
  year_data = pd.concat(states_data, axis=0) # Hier werden dann alle Jahre für ein Bundesland zusammengebracht
  full_data.append(year_data) # Hier werden alle DataFrames hinzugefügt

# Alle DataFrames werden nacheinander gemerged und doppelte Spalten ausgeschlossen, sowie die Formatierung und Null Werte überarbeitet.
last_df = full_data[0] 
for i in full_data[1:]:
  df = pd.merge(left=last_df, right=i, on="Datum", how="outer")
  df["Feiertag_x"].fillna(df["Feiertag_y"], inplace=True)
  df["Hinweis_x"].fillna(df["Hinweis_y"], inplace=True)
  df.drop(["Feiertag_y", "Hinweis_y"], axis=1, inplace=True)
  df.rename(columns={"Feiertag_x": "Feiertag", "Hinweis_x":"Hinweis"}, inplace=True)
  last_df = df

# Bei Feiertagen, die es nur in bestimmten Bundesländer gibt ist der Wert bei Länder, die diesen Tag nicht feiern Null
# Daher werden Null Values in Integer 0 umgewandelt.
df.fillna(0, inplace=True)
df

# Zuletzt wird der fertige DataFrame als csv Datei abgespeichert.
df.to_csv("deutsche_feiertage__2000_2030.csv", index=False)