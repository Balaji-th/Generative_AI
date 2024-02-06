import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# env access for Google AI Studio
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def getBotResponse(question):
    response = chat.send_message(question,stream=False)
    return response


if __name__ == '__main__':
    # Load the chat model
    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat(history=[])

    st.set_page_config(page_title="Q&A Bot", page_icon=":robot:")
    html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Google Gemini Q&A Bot</h2>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    ques = st.text_input("Input: ",key="input")
    submit = st.button("Ask Your question")

    # Initialize Session State for chat history
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    if submit and input:
        st.session_state["chat_history"].append(("You: ", ques))
        response = getBotResponse(ques)
        st.header("The Bot Response: ")
        for chunk in response:
            st.write(chunk.text)
            st.session_state["chat_history"].append(("Bot: ",chunk.text))
    st.header("Chat History: ")
    for role,resp in st.session_state["chat_history"]:
        st.write(f"{role}{resp}")







