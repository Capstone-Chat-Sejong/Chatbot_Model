import streamlit as st
from streamlit_chat import message
import requests

st.set_page_config(
    page_title="Streamlit Chat - Demo",
    page_icon=":robot:"
)

#openai.api_key = st.secrets["api_secret"]
headers = {"Authorization": st.secrets['api_key']}

st.header("Sejong Smart Assistant")
st.markdown("[Github](https://github.com/Capstone-Chat-Sejong/Chatbot_Model)")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def generate_response(prompt):
    text = 'generated text'
    # cosine similarity // token
    message = text
    return message 

def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text 


user_input = get_text()

if user_input:
    output = generate_response(user_input)
    # store the output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')