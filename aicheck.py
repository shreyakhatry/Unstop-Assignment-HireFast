import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import openai


# Set page configuration and title for Streamlit
st.set_page_config(page_title="HireFast", page_icon="", layout="wide")

# Add header with title and description
st.markdown(
    '<p style="display:inline-block;font-size:40px;font-weight:bold;">HireFast </p>'
    ' <p style="display:inline-block;font-size:16px;">HireFast is tool to assist students '
    'and companies use large csv data and ask natual language questions and visualize it. <br><br></p>',
    unsafe_allow_html=True
)

# We use pandasai which internally calls OpenAI, we do not need to explicity query
# before to any vector DB and pandasai internally gives best possible context and 
# calls OpenAI to get the best possible answer.
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def chat_with_csv(df, prompt):
    llm = OpenAI(api_token=OPENAI_API_KEY)
    pandas_ai = PandasAI(llm)
    result = pandas_ai.run(df, prompt=prompt)
    print(result)
    return result

input_csv = st.file_uploader("Upload your data CSV file", type=['csv'])

if input_csv is not None:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.info("CSV Uploaded Successfully")
        data = pd.read_csv(input_csv)
        st.dataframe(data, use_container_width=True)

    with col2:
        st.info("Chat Below")
        input_text = st.text_area("Enter your query")

        if input_text is not None:
            if st.button("Chat with CSV"):
                st.info("Your Query: " + input_text)
                result = chat_with_csv(data, input_text)
                st.success(result)

# Hide Streamlit header, footer, and menu
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)