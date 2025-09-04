import os
import streamlit as st
from dotenv import load_dotenv
import requests
import uuid

load_dotenv()
agent_api_key = os.getenv("AGENT_API_KEY")
agent_api_url = os.getenv("AGENT_URL")
# agent_api_url = 'http://localhost:5678/webhook-test/ea999fea-42dd-4b26-a1d4-183f13b8032b'

st.title('이메일 에이전트')

if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.write(msg['content'])

prompt = st.chat_input('이메일 내용을 입력해주세요')

if prompt:
    st.chat_message('user').write(prompt)
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    response = requests.post(
        agent_api_url,
        headers = {'Authorization': agent_api_key},
        json = {
                'message': prompt,
                'session_id': st.session_state.session_id
                }
        )
    
# request.post => 서버에 데이터를 전송하고 그에 대한 응답을 받아오기 위한 함수 
# agent_api_url에 접속을 하고 header 안에 있는 Authorization을 통해 인가를 받는다. 
# json형식으로 'message'항목에 prompt를 전달하고 'session_id'에 현재 session_id를 전달하는 과정을 수행 
# 전달받은 이후에 n8n에 존재하는 Openai를 통해 결과를 받는 것인데, 결과는 Output을 저장되는 것이다.
 
    st.session_state.messages.append({'role': 'assistant', 'content': response.json()['output']})
    with st.chat_message('assistant'):
        st.write(response.json()['output'])