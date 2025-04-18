import streamlit as st
import requests
import pandas as pd
import altair as alt

Key = "wqNZrkUHPRSYmX/GZ8Nr/piaYDRKsScgm6b8dMcNknkZ4G//n9cZU/zYqL1f3rLH"
headers = {"Authorization": f"Bearer {Key}"}

st.title("Explore the history of College Football.")

st.subheader("All data from CollegeFootballData.com API")

st.subheader("Week 1 AP Rankings Since 1950 🏈")

years = list(range(1950, 2025))
userYear = st.selectbox("Select a Year", reversed(years))

@st.cache_data
def getAP(year):
    link = (f"https://api.collegefootballdata.com/rankings?year={year}")
    response = requests.get(link, headers = headers)
    return response.json()

def extractAP(rankings):
    for week in rankings:
        if week["week"] == 1:
            for poll in week["polls"]:
                if poll["poll"] == "AP Top 25":
                    return poll["ranks"]
    return []

rankings = getAP(userYear)
finalAP = extractAP(rankings)

table = pd.DataFrame(finalAP)[["rank", "school", "points", "firstPlaceVotes"]]
table.columns = ["Rank", "School", "Points", "1st Place Votes"]
table.set_index("Rank", inplace=True)
st.dataframe(table, use_container_width=True)

st.write("")

def JeremiahSmith():
    Smith = "Images/JSmith.jpg"
    st.image(Smith, width = 800)
JeremiahSmith()

st.write("")

championTeams = ["Georgia", "Alabama", "LSU", "Clemson", "Ohio State", "Michigan"]

@st.cache_data
def getLocations():
    link = "https://api.collegefootballdata.com/teams/fbs"
    response = requests.get(link, headers=headers)
    return response.json()

teamData = getLocations()

champion_coords = []
for team in teamData:
    if team["school"] in championTeams:
        champion_coords.append({
            "School": team["school"],
            "lat": team["location"]["latitude"],   
            "lon": team["location"]["longitude"]  
        })

map_champs = pd.DataFrame(champion_coords)

st.subheader("Map of Recent National Champions 📍")
st.map(map_champs)
st.subheader("The Champs:")
st.markdown("""
- **Ohio State**: 2024, 2014  
- **Michigan**: 2023  
- **THWg**: 2022, 2021  
- **Alabama**: 2020, 2017, 2015  
- **LSU**: 2019  
- **Clemson**: 2018, 2016  
""")

st.write("")

def CalvinJohnson():
    CJ = "Images/CJJr.jpg"
    st.image(CJ, width = 800)
CalvinJohnson()

st.write("")

st.subheader("Final SP+ Ratings of the 2024 Season")
st.write("from Bill Connelly, via API")

conferences = [
    "ACC", "Big 12", "Big Ten", "SEC", "Pac-12",
    "Conference USA", "Mid-American", "Mountain West",
    "FBS Independents", "Sun Belt", "American Athletic"
]

SelectedConfs = st.multiselect(
    "Filter by Conference(s):",
    options=conferences,
    default=["ACC"]  
)

@st.cache_data
def getSP():
    link = "https://api.collegefootballdata.com/ratings/sp?year=2024"
    response = requests.get(link, headers=headers)
    return response.json()

@st.cache_data
def getTeams():
    link = "https://api.collegefootballdata.com/teams/fbs"
    response = requests.get(link, headers=headers)
    return response.json()

dataSP = getSP()
dataTeams = getTeams()

combinedSP = []
for team in dataSP:
    match = next((x for x in dataTeams if x["school"] == team["team"]), None)
    if match and match.get("conference") in SelectedConfs:
        combinedSP.append({
            "Team": team["team"],
            "Conference": match["conference"],
            "SP+ Rating": team["rating"]
        })

if combinedSP != []:
    frameSP = pd.DataFrame(combinedSP)
    frameSP = frameSP.sort_values("SP+ Rating", ascending=False)
    st.bar_chart(frameSP.set_index("Team")["SP+ Rating"])
else:
    st.write("No conferences selected!.")
