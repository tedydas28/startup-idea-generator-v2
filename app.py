import streamlit as st
import openai
import os

# Load the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit layout
st.set_page_config(page_title="Startup Idea Generator", page_icon="💡")
st.title("🚀 Startup Idea Generator")
st.write("Describe your interests, skills, or passions — and get a custom startup idea powered by AI.")

# User input
user_prompt = st.text_input("💬 What are you interested in?", placeholder="e.g. AI, climate, fashion, travel...")

# When button is pressed
if st.button("✨ Generate Startup Idea"):
    if not openai.api_key:
        st.error("❌ API key not found.")
    elif not user_prompt.strip():
        st.warning("Please enter your interests.")
    else:
        with st.spinner("Thinking..."):
            try:
                client = openai.OpenAI()

                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You're an expert startup mentor helping a student brainstorm creative startup ideas."},
                        {"role": "user", "content": f"I’m interested in {user_prompt}. Can you give me a creative and original startup idea based on this?"}
                    ],
                    temperature=0.8,
                    max_tokens=300
                )
                idea = response.choices[0].message.content
                st.success("Here's your startup idea:")
                st.markdown(idea)

            except Exception as e:
                st.error(f"⚠️ Error generating idea: {e}")
