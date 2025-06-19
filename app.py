import streamlit as st
import openai

# Replace with your actual API key
openai.api_key = "your-api-key-here"

st.title("Legal Contract Generator")

contract_type = st.selectbox("Choose contract type", ["Letter of Demand", "Simple Will", "Sale of Land Agreement"])
party_1 = st.text_input("Your Client's Name")
party_2 = st.text_input("Other Party's Name")
amount = st.text_input("Amount or Asset Description")
jurisdiction = st.text_input("Jurisdiction")
details = st.text_area("Details or Special Terms")

if st.button("Generate Contract"):
    prompt = f"""
    Generate a {contract_type} between {party_1} and {party_2}, in the jurisdiction of {jurisdiction}.
    If relevant, include an amount or asset description: {amount}.
    Special terms or context: {details}.
    Use formal, professional legal language.
    """
    with st.spinner("Generating..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        contract_text = response.choices[0].message.content
        st.subheader("Generated Contract")
        st.text_area("Contract Output", contract_text, height=400)
        st.download_button("Download Contract", contract_text, file_name="contract.txt")
