import streamlit as st
import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

# Načítanie OpenAI kľúča zo Secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.title("Edukácia: Montgomery T-tubus")
st.write("Dobrý deň. Som Váš digitálny asistent pre ošetrovateľskú starostlivosť o Montgomery T-kanylu(MTT). Som tu, aby som Vám pomohol s otázkami týkajúcimi sa základných informácií aj ošetrovateľských postupov na základe odborných študijných materiálov. Ako Vám dnes môžem pomôcť?")

# Funkcia na načítanie PDF z priečinka
@st.cache_resource
def load_data():
    all_docs = []
    for file in os.listdir("."):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(file)
            all_docs.extend(loader.load())
    
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(all_docs, embeddings)
    return vectorstore

# Spustenie a vyhľadávanie
try:
    vectorstore = load_data()
    qa_chain = RetrievalQA.from_chain_type(ChatOpenAI(model="gpt-3.5-turbo"), retriever=vectorstore.as_retriever())
    
    query = st.text_input("Napíš svoju otázku...")
    if query:
        with st.spinner("Hľadám v odborných materiáloch..."):
            response = qa_chain.invoke(query)
            st.write(response["result"])
except Exception as e:
    st.info("Zadajte otázku do políčka vyššie. (Ak sa vyskytla chyba s PDF, uistite sa, že sú nahrané v repozitári).")
