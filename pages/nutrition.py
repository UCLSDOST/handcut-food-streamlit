import streamlit as st

st.set_page_config(layout="wide")
st.header("Switch page worked!")

if st.button("back"):
    st.switch_page("main.py")

col1, col2 = st.columns([0.4, 0.6])

with col1:
    with st.container(border=True):
        st.write(
            """
            <div style="font-family: Helvetica, Arial, sans-serif;">
                Nutrition Facts
            </div>
            """,
            unsafe_allow_html=True,
        )