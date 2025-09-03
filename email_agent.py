import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
agent_api_key = os.getenv("AGENT_API_KEY")
agent_api_url = os.getenv("AGNET_API_URL")

st.title('이메일 에이전트')