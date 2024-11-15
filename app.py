import streamlit as slt
import os
from groq import Groq  
from langchain.chains import ConversationChain
from langchain_groq import ChatGroq  
from dotenv import load_dotenv

load_dotenv()


groq_api_key = os.environ['GROQ_API_KEY']



def main():
    slt.set_page_config(layout="wide")


    slt.title("MULTI FUNCTION CHATBOT")

    slt.markdown("""
    Welcome to the Multi-Function Chatbot! Ask me anything related to grammar, translations, programming, and more.
    """)

    

    user = slt.text_input("Ask a question...",  height=150, placeholder="Type your question here...")

    
    model_name = 'Gemma2-9b-It'

    groq_chat = ChatGroq(
        groq_api_key=groq_api_key,
        model_name=model_name
    )

    conversation = ConversationChain(
        llm=groq_chat,
    )

    if user:
        response = conversation(user)
        slt.markdown("### Chatbot Response:")
        slt.write( response['response'])
    

   


if __name__ == '__main__':
    main()
