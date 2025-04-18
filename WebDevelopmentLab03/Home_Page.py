import streamlit as st

# Title of App
st.title("Web Development Lab03")

# Assignment Data 
# TODO: Fill out your team number, section, and team members

st.header("CS 1301")
st.subheader("Team 18, Web Development - Section B")
st.subheader("Dev & Ezra")


# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. **Page Name**: Description
#       2. **Page Name**: Description
#       3. **Page Name**: Description
#       4. **Page Name**: Description

st.write("""
Welcome to our Streamlit Web Development Lab03 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. Home Page: The hub of our app, access the other pages from here. 
2. History Hub: Access the history of College Football through an interactive page. 
3. College Football Analysis - PLACE YOUR BETS!!
4. College Football Chatbot: The solution to all your college-football related queries. 

""")

def JustinThomas():
    homeimage = "Images/JT.jpg"
    st.image(homeimage, width = 1000)
JustinThomas()
