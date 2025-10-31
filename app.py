import streamlit as st
import google.generativeai as genai
import os

# --- API Key Setup ---
# NOTE: It's highly recommended to use environment variables for API keys in real applications.
# For simplicity, keeping the direct key setup as in your original 'app.py' for now.
API_KEY = "AIzaSyDwppW4aU9-ZazEkOAJjWpZ3jURH32MqVg" # Replace with your actual key or use os.environ

# Configure the Google Generative AI API
genai.configure(api_key=API_KEY)

# --- App Layout ---
st.title("Developed By: Mahesh ")
st.title("AI Code Reviewer")
st.write("Enter your code below for review and select the language:")

# 1. Language Selection Widget
selected_language = st.selectbox(
    "Select Programming Language:",
    ("Python", "Java", "C++", "C")
)

# Text area for code input
user_code = st.text_area(f"Enter your {selected_language} code here...", height=200)

# Button to trigger code review
if st.button("Generate"):
    if user_code:
        try:
            # Using the fast and capable 'gemini-2.5-flash' model
            llm = genai.GenerativeModel('gemini-2.5-flash')
            
            # Send the user code for review
            chatbot = llm.start_chat(history=[])
            
            # 2. Dynamic Prompt Modification based on selection
            prompt = (
                f"Review the following {selected_language} code. "
                "Identify any bugs, suggest improvements for best practices, "
                "and provide the complete, corrected code in a single markdown code block "
                f"with the language identifier: ```{selected_language.lower()}\n\n"
                f"Code to review:\n{user_code}"
            )
            
            response = chatbot.send_message(prompt)
            
            # Display the AI-generated response
            st.subheader("Code Review")
            st.write(f"Bug Report and Suggestions for **{selected_language}**:")
            # Use st.markdown to properly render the AI's response text and code block
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"An error occurred during the AI review: {e}")
            st.warning("Please check your API key, model name, and network connection.")
    else:
        st.warning("Please enter some code for review.")