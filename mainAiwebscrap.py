# import langchain
from scrape import scrape_website,split_dom_content,clean_body_content,extract_body_content
import streamlit as st
from parser import parse_with_ollama
st.title("AI Web scrapper")
url=st.text_input("Enter a web url")
if st.button("Scrap Site"):
    st.write("Scrapping Website...")
    result=scrape_website(url)
    # st.write(result)
    body_content=extract_body_content(result)
    cleaned_content=clean_body_content(body_content)
    st.session_state.dom_content = cleaned_content
    with st.expander("View dom contnt"):
        st.text_area("DOM content",cleaned_content,height=300)
    # st.write(cleaned_content)
if "dom_content" in st.session_state:
    parse_description=st.text_area("Please describe what you want to parse..")

    if st.button("Parse Contnt"):
        st.write("Parsing the content...")
        dom_chunks=split_dom_content(st.session_state.dom_content)
        # Passing to an llm
        result=parse_with_ollama(dom_chunks,parse_description)
        st.write(result)