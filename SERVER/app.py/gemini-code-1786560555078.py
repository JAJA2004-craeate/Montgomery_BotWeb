import streamlit as st

st.set_page_config(page_title="Asistent pre Montgomery T-kanylu")

st.title("Edukácia: Montgomery T-tubus")

# Tvoj systémový prompt
system_prompt = """
Si odborný asistent pre ošetrovanie Montgomery T-tubusu v domácom prostredí. 
Odpovedaj študentom medicíny, sestrám, pacientom výlučne na základe nahraných dokumentov. 
Ak informáciu v dokumentoch nenájdeš, slušne to povedz. 
Buď profesionálna, stručná a presná. 
... (tu vložíš celý zvyšok svojho promptu o videu a núdzových stavoch)
"""

st.write("Vitaj! Som tu, aby som ti pomohla s ošetrovaním kanyly.")

# Chatovacie pole
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Napíš svoju otázku..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Tu bude logika, ktorá napojí bota na tvoje PDF a AI model
    response = "Tu bude odpoveď od tvojej AI..." 
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})