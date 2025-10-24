"""
Mohammed Azhar
Oct 22, 2025
lab 11, APIs

"""
import pandas as pd

# --------
# 1. example dataframe
# --------
dict_ ={'a': [11,21,31], 'b': [12,22,32]}

#create a dataframe for dict_
df = pd.DataFrame(dict_)

#display the first few rows of the dataframe 
print(df.head())

# mean method calculates and returns the mean of the data 
print(df.mean())

# ---------------
# 2. Get NBA teams 
# ---------------
from static import get_teams


# the method get_teams() returns a list of dictionaries 
nba_teams = get_teams()
print(f"First 2 teams: {nba_teams[:2]}")

#convert list of dictionaries into dataframe 
df_teams = pd.DataFrame (nba_teams)
print (df_teams.head())

#find the id of the warriors
df_warrior = df_teams[df_teams["nickname"] == "Warrior"]
print(df_warrior)

#find the id of the warriors using the information in the first column 
warrior_id = df_warrior[["id"]].values [0][0]
print(f"\n Warrior id = {warrior_id}")

#----------------
# 3. download the pickle file
# --------------

import requests

url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl" 

file =_name = "Golden_Sate.pk1"

print("\nDownloading external data")
response = requests.get(url)

if response.status_code == 200:
    with open(file_name,"wb") as f:
        f.write(response.content)
    print("download complete")

else:
    print("Download failed")

# b. load dataframe from pickle
games = pd.read_pickle(file_name)
print("\n Games data from pickle file:")
print(games.head())

# c. filter GSW vs Raptors 
warriors_vs_raptors = games[games['MATCHUP'].str.contains("TOR") ]



gsw_home_vs_raptors = warriors_vs_raptors[warriors_vs_raptors["MATCHUP"].str.contains("vs .")]
gsw_away_vs_raptors = warriors_vs_raptors[warriors_vs_raptors["MATCHUP"].str.contains("@")]

#d. calculate averages 

home_avg_plus = gsw_home_vs_raptors['PLUS_MINUS'].mean()
away_avg_plus = gsw_away_vs_raptors['PLUS_MINUS'].mean()
home_avg_pts = gsw_home_vs_raptors['PTS'].mean()
away_avg_pts = gsw_home_vs_raptors['PTS'].mean()    

print(f"\nWarriors home average {home_avg_plus}")
print(f"\nWarriors home average {away_avg_plus}")

# e. visualization
import matplotlib.pyplot as plt

metrics = ["PLUS_MINUS", 'PTS']
home_values = [home_avg_plus, home_avg_pts]
away_values = [away_avg_plus, away_avg_pts]

x= range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8,5))
plt.bar( [i - bar_width/2 for i in x],home_values, width=bar_width,label = "Home", color = "skyblue")
plt.bar( [i + bar_width/2 for i in x],home_values, width=bar_width,label = "Home", color = "skyblue")

plt.xticks(x,metrics)
plt.title("Golden State Warriors vs Raptors - Home vs Away comparison")
plt.ylabel("Average Value")
plt.legend()
plt.grid(Axis="y", linestyle = "--", alpha=0.7)
plt.tight_layout()
plt.show()

input("Press Enter to Close")