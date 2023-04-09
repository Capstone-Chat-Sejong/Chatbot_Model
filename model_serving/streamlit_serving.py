import streamlit as st
from streamlit_chat import message
import requests
import torch
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="Streamlit Chat - Demo",
    page_icon=":robot:"
)

st.title("Sejong Smart Assistant- Demo")
st.subheader("세종 스마트 어시스턴트 데모사이트")
st.markdown("[Github - 소스코드 확인](https://github.com/Capstone-Chat-Sejong/Chatbot_Model)")

# model 불러오기
@st.cache(allow_output_mutation=True)
def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    LOAD_MODEL = torch.load("model.pt", map_location=device)
    return LOAD_MODEL

# 저장 데이터 불러오기
@st.cache(allow_output_mutation=True)
def get_dataset():
    df = pd.read_csv('test_embedding.csv', encoding = 'cp949')
    # 임베딩값 텐서 리스트 형태로
    embedding_data = torch.tensor(df['embedding_vector'].tolist())
    return embedding_data
    
model = load_model()
embedding_data = get_dataset()

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def scoring_method(input_text):
    user_encode = model.encode(input_text)
    user_tensor = torch.tensor(user_encode)
    
    cos_sim = cosine_similarity(user_tensor, embedding_data)
    
    best_sim_idx = int(np.argmax(cos_sim))
    selected_A = embedding_data['답변'][best_sim_idx]
    
    return selected_A
    

with st.form('form', clear_on_submit=True):
    user_input = st.text_input('당신 : ', '')
    submitted = st.form_submit_button('전송')


if submitted and user_input:
    answer = scoring_method(user_input)
    # 유저와 챗봇의 대화 내용을 저장
    st.session_state.past.append(user_input)
    st.session_state.generated.append(answer)

# 저장된 대화 내용 보여주기
for i in range(len(st.session_state['past'])):
    message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
    if len(st.session_state['generated']) > i:
        message(st.session_state['generated'][i], key=str(i) + '_bot')



# if __name__ == '__main__':
# 	main()