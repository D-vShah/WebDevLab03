import requests as re
from pprint import pprint
import streamlit as st

Univ = re.get('https://akabab.github.io/superhero-api/api/all.json')
Peeps = Univ.json()
count1 = 0
count2 = 0
count3 = 0
st.header('What Heroes/Villains Share Your Similarities?')
st.info(
    "Answer these 3 questions and we will tell you which heroes/villains you are like, how many are like you, and what you're most likely to be!")  # NEW

Eyes = st.selectbox('What is your eye color?', (
'Yellow', 'Blue', 'Green', 'Brown', 'Red', 'Violet', 'White', 'Purple', 'Black', 'Silver', 'Yellow / Red', 'Grey',
'Yellow (without irises)', 'Gold', 'Blue / White', 'Hazel', 'Green / Blue', 'White / Red', 'Indigo', 'Amber',
'Yellow / Blue'))  # NEW
Hair = st.selectbox('What is your hair color?', (
'No Hair', 'Black', 'Blond', 'Brown', 'White', 'Purple', 'Orange', 'Pink', 'Red', 'Auburn', 'Strawberry Blond', 'Blue',
'Green', 'Magenta', 'Brown / Black', 'Silver', 'Grey', 'Orange / White', 'Yellow', 'Brown / White', 'Brownn', 'Gold',
'Red / Orange', 'Indigo', 'Red / White', 'Black / Blue'))
Gender = st.selectbox('What is your gender?', ('Male', 'Female', 'Other'))

if Gender == 'Other':
    Gender = '-'

if Hair:
    for thing in Peeps:
        if Eyes.lower() == thing['appearance']['eyeColor'].lower() and Hair.lower() == thing['appearance'][
            'hairColor'].lower() and Gender.lower() == thing['appearance']['gender'].lower():
            if thing['biography']['alignment'].lower() == 'good':
                st.write(f"You are similar to {thing['name']}, who is a hero!")
                count1 += 1
            elif thing['biography']['alignment'].lower() == 'bad':
                st.write(f"You are similar to {thing['name']}, who is a villain!")
                count2 += 1
            else:
                st.write(f"You are similar to {thing['name']}, who is neutral!")
                count3 += 1
            st.image(f"{thing['images']['lg']}")

    if count1 == count2 == count3 == 0:
        st.write("You're completely original")
    else:
        st.write(f"Superheros like you: {count1}")
        st.write(f"Villains like you: {count2}")
        st.write(f"Neutrals like you: {count3}")
        if count1 > count2:
            end = 'hero'
        elif count1 < count2:
            end = 'villain'
        else:
            end = 'neutral'
        st.write(f"You are most likely to be a {end}!")

user_input = st.text_input("Expecting someone else? Type their name down here!")  # NEW

found = False
for thing in Peeps:
    if len(user_input) != 0:
        if user_input.lower() in thing['name'].lower() or user_input.lower() in thing['biography'][
            'fullName'].lower() or user_input.lower() in thing['biography']['aliases']:
            st.write(f"This one? {thing['name']} is one of the {thing['biography']['alignment']} guys!")
            st.image(f"{thing['images']['lg']}")
            found = True

if found == False and len(user_input) != 0:
    st.write('Who? (Beware of hyphenated names and one-word names that seem like two words!)')