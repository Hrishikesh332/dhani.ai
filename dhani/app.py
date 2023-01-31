import streamlit as st
import os
from streamlit_option_menu import option_menu
import cohere

selected = option_menu(
    menu_title=None,
    options=["Home","Dhani Content"],
    menu_icon=None,
    orientation="horizontal")
if (selected=="Home"):
    st.header("Welcome to Dhani.ai!")
    st.write('''
    Are you tired of spending hours creating financial content? Look no further than Dhani.ai
    ''')
    st.write("Our Dhani prompt uses advanced artificial intelligence to generate financial content")

if (selected=="Dhani Content"):
    st.subheader("You're at the right place to get the content of any question in this whole finance universe!!!")
    question=st.text_area("Add your topic below!!!")
    button=st.button("Answer")

    def response1(ques):
        cohere.api_key = cohere.Client("")

        response = cohere.api_key.generate(  
        model='command-xlarge-20221108',  
        prompt = question,  
        max_tokens=500,  
        temperature=1.0,  
        stop_sequences=["--"]
        )
        
        print(response)
        return response.generations[0].text
    if question and button:
        reply=response1(question)
        st.write(reply)