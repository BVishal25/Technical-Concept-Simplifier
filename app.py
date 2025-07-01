import streamlit as st
import openai
import google.generativeai as genai 

# openai API key for connecting to the LLM
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else None

#function to get response from the LLM
def simplify_text(text_to_simplity, target_audience, api_key):
    openai.api_key = api_key

    system_prompt = """
    You are an expert technical communicator and simplifier. Your goal is to make complex technical documentation or concepts
    and explain them clearly and concisely to a specific audience.
    
    Given a piece of technical text and a target audience, rephrase the text.
    - Simplify Jargon: Replace or explain technical jargon in simple terms.
    - Analogies/Examples: Use appropriate analogies or real-world examples relevant to the target audience.
    - Conciseness: Be concise while retaining accuracy.
    - Audience Tone: Adapt the tone and vocabulary to the audience.

    Output the simplified explanation directly, without conversational filler."""

    messages = [
        {"role": "system", "content" : system_prompt},
        {"role": "user", "content" : f"Original text:{text_to_simplity}\n\nTarget Audience:{target_audience}"}
    ]

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"
    
st.set_page_config(page_title="Technical Content Simplifier AI Agent", layout="wide")

st.title("💡 Technical Concept Simplifier AI Agent")
st.markdown("Enter complex technical text below, choose your audience, and let AI simplify for you!")

#user input for text
col1, col2 = st.columns(2)
with col1:
    st.subheader("Original Technical Text")
    original_text = st.text_area("Paste your text here:", height=300, key="original_text_input")

with col2:
    st.subheader("Target Audience")
    target_audience = st.selectbox(
        "Who are you explaining this to?",
        ("Non-technical Manager", "High School Student", "Beginner Developer", "General Public", "Domain Expert (for concise overview)"),
        key="audience_select"
    )
    st.markdown(f"*(Selected audience: {target_audience})*")

    #simplify button
    if st.button("Simplify Concept", type="primary"):
        if original_text:
            with st.spinner("Simplifying..."):
                simplified_text = simplify_text(original_text, target_audience, OPENAI_API_KEY)
            st.subheader("Simplified Explanation")
            st.write(simplified_text)
        else:
            st.warning("Please enter some text to simplify.")

st.markdown("---")
st.markdown("Built with ❤️ by an AI Enthusiast using openai, streamlit, and prompt techniques.")