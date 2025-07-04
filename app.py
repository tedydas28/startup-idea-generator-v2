import streamlit as st
import openai
import os

# Load the API key from environment variable (set via Streamlit secrets or .env)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit app layout
st.set_page_config(page_title="Startup Idea Generator", page_icon="💡")
st.title("🚀 Startup Idea Generator")
st.write("Describe your interests, skills, or passions — and get a custom startup idea powered by AI.")

# Input box
user_prompt = st.text_input("💬 What are you interested in?", placeholder="e.g. AI, climate, fashion, travel...")

# Button
if st.button("✨ Generate Startup Idea"):
    if not openai.api_key:
        st.error("❌ Missing OpenAI API key. Please set OPENAI_API_KEY in your Streamlit secrets.")
    elif not user_prompt.strip():
        st.warning("Please enter something you're interested in.")
    else:
        with st.spinner("Thinking..."):
            try:
                # Call OpenAI's GPT model
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You're an expert startup mentor helping a student brainstorm creative startup ideas."},
                        {"role": "user", "content": f"I’m interested in {user_prompt}. Can you give me a creative and original startup idea based on this?"}
                    ],
                    temperature=0.8,
                    max_tokens=300
                )
                idea = response.choices[0].message["content"]
                st.success("Here's your startup idea:")
                st.markdown(idea)

            except Exception as e:
                st.error(f"⚠️ Error generating idea: {e}")
