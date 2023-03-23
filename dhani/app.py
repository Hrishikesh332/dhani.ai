import streamlit as st
import os
from streamlit_option_menu import option_menu
import cohere

page_element="""
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://wallpapercave.com/wp/wp6907416.jpg");
background-size: cover;
}
[data-testid="stMarkdownContainer"]{
background-color: rgba(23,231,12,131);
}

[data-testid="stHeader"]{
background-color: rgba(0,0,0,0);
}
[data-testid="stSidebar"]> div:first-child{
background-image: url("https://th.bing.com/th/id/OIP.8ZY46JwA7_kiFkDNEfSM6AHaNJ?pid=ImgDet&rs=1");
background-size: cover;
}
</style>
"""
st.markdown(page_element, unsafe_allow_html=True)

with st.sidebar:
    st.image("https://github.com/Hrishikesh332/dhani.ai/blob/main/dhani/logodhani.png")
    
selected = option_menu(
    menu_title=None,
    options=["Home","Dhani Content"],
    menu_icon=None,
    orientation="horizontal")
if (selected=="Home"):
    st.header("Welcome to Dhani.ai!")
    st.write('''
    Dhani.ai" is a cutting-edge financial content generation platform powered by Cohere's advanced Text Generation API. 
    The platform leverages the power of NLP and AI to provide its users with high-quality, insightful and accurate financial content in real-time.
    
    With Dhani.ai, users can generate financial reports, news articles, investment research and other types of financial content in minutes, freeing up their time to focus on more strategic tasks.
    
    Whether you're an investment banker 💼, financial analyst💹, or portfolio manager💰, Dhani.ai is the perfect tool to help you stay ahead of the curve and stay informed about the latest trends and developments in the financial world. With its easy-to-use interface and intuitive customization options, Dhani.ai is the ideal solution for anyone looking to streamline their financial content creation process. 
    
    Get started today and experience the future of financial content generation with Dhani.ai🚀.
    ''')
    st.write("Our Dhani prompt uses advanced artificial intelligence to generate financial content")

if (selected=="Dhani Content"):
    st.subheader("You're at the right place to get the content of any question in this whole finance universe!!!")
    question=st.text_area("Add your topic below!!!")
    button=st.button("Answer")

    def response1(ques):
        s=st.secrets['API']
        cohere.api_key = cohere.Client(s)

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
