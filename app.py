import streamlit as st 
from dotenv import load_dotenv 
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint 
 
# Load environment variables (HF_TOKEN) 
load_dotenv() 

# Page setup
st.set_page_config(page_title="AI Summarizer - Static Prompt", page_icon="📝")

# Simple styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 24px;
        width: 100%;
    }
    .info-box {
        background-color: #e3f2fd;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #2196F3;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)
 
# Create HuggingFace Cloud API connection 
llm = HuggingFaceEndpoint( 
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  # Open-source model
    task="text-generation", 
    max_new_tokens=150, 
    temperature=0.7 
) 
 
# Wrap HF endpoint into LangChain chat interface 
model = ChatHuggingFace(llm=llm) 
 
# UI
st.title("📝 AI Text Summarizer")
st.write("**Learning Project: Static Prompt Approach**")

# Info box explaining static vs dynamic
st.markdown("""
    <div class="info-box">
        <strong>🎯 Learning Goal:</strong> Understanding <strong>Static Prompts</strong><br>
        <small>In this version, the user directly enters their prompt/text. 
        This is different from dynamic prompts where the app adds context or instructions automatically.</small>
    </div>
""", unsafe_allow_html=True)

st.write("**Tech Stack:** HuggingFace Cloud API (Open Source) + LangChain + Streamlit")
 
user_input = st.text_area(
    "Enter your text or prompt:", 
    placeholder="Example: Summarize the attention mechanism in 5 lines...",
    height=100
) 
 
if st.button("✨ Generate Summary"): 
    if user_input: 
        with st.spinner("Processing with AI..."):
            result = model.invoke(user_input)  # Static: sends exactly what user typed
            st.success("✅ Summary Generated!")
            st.write(result.content) 
    else: 
        st.warning("⚠️ Please enter a prompt.") 

st.markdown("---")
st.caption("Built with Streamlit + HuggingFace + LangChain | Learning Project")
 
# To run: streamlit run app.py
