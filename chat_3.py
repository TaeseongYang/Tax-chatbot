import streamlit as st
from dotenv import load_dotenv
from llm_2 import get_ai_response

load_dotenv()

st.set_page_config(page_title='langchain을 활용한 chatbot', page_icon = '🤖')

st.title('🤖 Inflearn Chatbot')
st.caption("소득세법과 관련된 질문에 대한 답변을 해드립니다!")

if 'message_list' not in st.session_state:
    st.session_state.message_list = []

for message in st.session_state.message_list:
    with st.chat_message(message['role']):
        st.write(message['content'])

if user_question := st.chat_input(placeholder = "소득세법과 관련된 질문을 해주세요!"):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({'role':'user', 'content':user_question})

    with st.spinner('답변을 생성하는 중입니다.'):
        ai_response = get_ai_response(user_question)

        with st.chat_message('ai'):
            ai_message = st.write_stream(ai_response) # 최종으로 나온 전체 답변을 넣어줘야 하는 것임.
        st.session_state.message_list.append({'role':'ai', 'content': ai_message})