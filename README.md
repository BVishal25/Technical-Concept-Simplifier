# Project Title & Description: 
Technical Concept Simplifier AI Agent 
- An AI-powered tool to break down complex technical jargon for various audiences.

# Features:
- Simplifies technical text based on audience.
- Supports various target audiences (e.g., non-technical, beginner, expert).
- Intuitive web interface.
- Leverages advanced Prompt Engineering techniques.

# Technologies Used: 
- Python
- Streamlit
- Gemini AI (gemini-1.5-flash-latest) 

# How to Run Locally: 
First install the requirement packages
```pip install -r requirements.txt```
Then run it on streamlit
```streamlit run app.py.```

# Demo: 
If you deploy it, link to the live app!

# Prompt Engineering Insights:
1. In this project, I used prompt techniques that I learned from deeplearning.AI course 'ChatGPT Prompt Engineering for Developers'
2. First, I specifically mentioned what is gemini's role and what it needs to focus on.
3. Then, I gave user input and user's target audience.
4. Then, I pointed it out its core capabilities and stated it to maintain accuracy, integrity and adapt to tone of the audience.
5. Finally, I added not to use conversational filler (ie. you know, ah, oh...)

# Future Enhancements:
Instead of manually copy pasting the complicated and technical text, it can read the uploaded document that are complex and provide the results according to the audience's tone.  