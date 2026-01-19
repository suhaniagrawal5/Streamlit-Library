import streamlit as st
st.title("chai taste poll")
col1, col2=st.columns(2)
with col1:
    st.header("masala chai")
    vote1= st.button("vote masala chai")

with col2:
    st.header("adrak chai")
    
    vote2= st.button("vote adrak chai")

if vote1:
    st.success("Thanks for voting masala chai")
elif vote2:
    st.success("Thanks for voting adrak chai")
