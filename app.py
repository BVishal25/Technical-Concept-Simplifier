import streamlit as st
import google.generativeai as genai 

# gemini API key for connecting to the LLM and error handling
if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    st.error("Google Gemini API key not found in .streamlit/secrets.toml or Streamlit Cloud secrets.")
    st.stop()

#function to get response from the LLM
def simplify_text(text_to_simplify, target_audience):
    model = genai.GenerativeModel('gemini-1.5-flash-latest')

    prompt_parts = f"""You are an expert technical communicator and simplifier. 
    Your goal is to take complex technical documentation or concepts and explain them clearly 
    and concisely to a specified audience.
    
    Given the following technical text:
    ---
    {text_to_simplify}
    ---
    Please rephrase this text for a **{target_audience}**.

    Ensure you:
    - Simplify jargon: Replace or explain technical jargon in simple terms.
    - Use appropriate analogies or real-world examples relevant to that audience.
    - Be concise while retaining accuracy.
    - Adapt the tone and vocabulary to the chosen audience.

    Provide the simplified explanation directly, without conversational filler."""

    # getting response from the gemini model
    try:
        response = model.generate_content(prompt_parts)
        return response.text.strip() 

    except Exception as e:
        return f"An error occurred with Gemini API: {e}"
    
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
                simplified_output = simplify_text(original_text, target_audience)
            st.subheader("Simplified Explanation")
            st.write(simplified_output)
        else:
            st.warning("Please enter some text to simplify.")

st.markdown("---")
st.markdown("Built with ❤️ by an AI Enthusiast using gemini model, streamlit, and prompt techniques.")