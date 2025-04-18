from google import genai
import streamlit as st
import requests as re
import os

key = "AIzaSyAy6sFFUw_13RsHoXEKRbyComrs81QQ8fY"
Univ = re.get('https://akabab.github.io/superhero-api/api/all.json')
Peeps = Univ.json()

user_input = st.text_input(
    "Gem is going to tell you where and how a character of your choice first appeared. But first, we need to find them! Type your character below!")  # NEW

found = False
lisst = []
for thing in Peeps:
    if len(user_input) != 0:
        if user_input.lower() in thing['name'].lower() or user_input.lower() in thing['biography'][
            'fullName'].lower() or user_input.lower() in thing['biography']['aliases']:
            lisst.append(thing['name'])
if lisst != []:

    hero = st.selectbox('Which of these?', tuple(lisst), index=None)

    if hero != None:
        st.write(f'You have selected {hero}! Now Gem will explain their first appearance!')
        for thing in Peeps:
            if thing['name'] == hero:
                appearance = thing['biography']['firstAppearance']
                break
        try:

            genai.configure(api_key=key)
            model = genai.GenerativeModel("gemini-1.5-flash")  # this is the free model of google gemini
            response = model.generate_content(f"Explain {hero}'s first appearance in {appearance}.")
            st.write(response.text)

            if 'messages' not in st.session_state:
                st.session_state.messages = []

            for message in st.session_state.messages:
                with st.chat_message(message['role']):
                    st.markdown(message['content'])

            talk = st.chat_input("Ask or Say Anything!")
            if talk:
                st.chat_message("user").markdown(talk)
                st.session_state.messages.append({'role': 'user', 'content': talk})
                response = model.generate_content(f"{talk}.")

                with st.chat_message('assistant'):
                    st.markdown(response.text)
                st.session_state.messages.append({'role': 'assistant', 'content': response.text})


        except:
            st.write("Seems Gem is overwhelmed. Please come back later.")

elif len(user_input) > 0:
    st.write(
        'We are unable to find this character. (Beware of hyphenated names and one-word names that appear to be two words)')
