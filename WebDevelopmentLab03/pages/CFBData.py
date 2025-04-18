import streamlit as st
import requests
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=st.secrets["AIzaSyAeFwEOr_vXUml6LsbAZ-Gp-vvmc87Bnak"])
model = genai.GenerativeModel('gemini-pro')

# API setup
CFB_KEY = st.secrets["CFB_KEY"]
headers = {"Authorization": f"Bearer {CFB_KEY}"}

st.title("🏈 Gemini CFB Analysis")

# User inputs
team1 = st.text_input("Enter Team 1", "Georgia")
team2 = st.text_input("Enter Team 2", "Alabama")
year = st.slider("Select Season", 2010, 2024, 2023)

@st.cache_data
def get_matchup_data(team1, team2, year):
    url = f"https://api.collegefootballdata.com/teams/matchup?team1={team1}&team2={team2}&minYear={year}"
    response = requests.get(url, headers=headers)
    return response.json()

# Fetch data and generate analysis
if st.button("Analyze Matchup"):
    data = get_matchup_data(team1, team2, year)
    prompt = f"""
    Analyze this college football matchup data: {data}.
    Compare {team1} and {team2} in {year}. Highlight key stats, strengths, and weaknesses.
    Write a ESPN-style analysis in 3 sentences.
    """
    with st.spinner("Generating analysis..."):
        response = model.generate_content(prompt)
        st.subheader(f"{team1} vs {team2} {year} Analysis")
        st.markdown(f"```{response.text}```")