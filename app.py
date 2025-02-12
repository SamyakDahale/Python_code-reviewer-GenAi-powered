import streamlit as st
import google.generativeai as genai

f = open("API_key.txt")
key = f.read() # Create a txt file in the same folder name "API_key.txt"
genai.configure(api_key=key)


# Streamlit UI creation
st.title("Python Code Review AI")
st.subheader("Submit your Python code for AI-powered bug detection and fixes")

user_code = st.text_area("Paste your Python code here:", height=200)

# File uploader # addiditnal functionality
uploaded_file = st.file_uploader("Or upload a .py file", type=["py"])

if uploaded_file:
    user_code = uploaded_file.read().decode("utf-8")  #  file content reading

def review_code(code):
    
    model = genai.GenerativeModel("gemini-pro")  # You may choose any gemini model of ur chouce
    response = model.generate_content(f"Review this Python code and suggest improvements:\n\n{code}")
    return response.text  


if st.button("Review Code "):
    if user_code.strip():
        with st.spinner("Analyzing your code..."):
            feedback = review_code(user_code)  # Get AI-generated feedback
            
        # Display results
        st.subheader(" Code Review & Suggestions")
        st.write(feedback)
    else:
        st.warning(" Please enter or upload Python code before submitting.")

