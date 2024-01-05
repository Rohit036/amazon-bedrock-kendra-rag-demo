import streamlit as st

st.set_page_config(
    page_title="IBM DEMO"
)

c1, c2 = st.columns([1, 8])
with c1:
    st.image("./images/bedrock.png", width=70)

with c2:
    st.markdown("<h2 style='text-align: left; line-height: 10pt'>Onboarding onto MCC.</h2>", unsafe_allow_html=True)
    st.caption("Q&A application")
    
st.sidebar.success("Select an option above ☝️")
