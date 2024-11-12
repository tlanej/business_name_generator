import os
import random
import openai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API (Assuming the API key is saved securely)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate business names using OpenAI API
def generate_business_name(keywords, industry, style):
    prompt = f"Generate unique business names for a company in the {industry} industry using the following keywords: {keywords}. The names should be {style}."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0.7,
        n=5
    )
    business_names = [choice['message']['content'].strip() for choice in response['choices']]
    return business_names

# Streamlit app definition
def main():
    st.title("AI/ML Business Name Generator")
    st.write("Welcome! Let's generate some amazing names for your AI/ML business.")

    # Inputs for keywords, industry, and style
    keywords = st.text_input("Enter some relevant keywords for your business:", "AI, Machine Learning, Data")
    industry = st.text_input("Enter your business's industry:", "Technology")
    style = st.selectbox(
        "What style of business name are you looking for?",
        ("creative", "professional", "modern", "fun", "short and catchy")
    )

    # Button to generate business names
    if st.button("Generate Business Names"):
        if keywords and industry:
            with st.spinner('Generating names...'):
                names = generate_business_name(keywords, industry, style)
                st.write("### Here are some suggested business names:")
                for name in names:
                    st.success(name)
        else:
            st.warning("Please fill in both keywords and industry.")

    # Example or Random Idea Button
    if st.button("Give me a random idea!"):
        random_keywords = random.choice(["Cloud", "AI", "Tech", "Neural", "Predictive"])
        random_industry = random.choice(["Healthcare", "Finance", "Retail", "Education", "Entertainment"])
        st.write(f"Here are some random ideas: Keywords - {random_keywords}, Industry - {random_industry}")

# Run the app
if __name__ == "__main__":
    main()
