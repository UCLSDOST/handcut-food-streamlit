import streamlit as st

st.title('Menu (Mock)')
st.write("---")

week = st.selectbox(
    "Select Week",
    ("1", "2", "3")
)

if week == "1":
    with st.container(border=True):
        st.write("Allergen Guide: put info here for vegan / gf etc")

    col1, col2 = st.columns(spec=[0.4, 0.6])

    with col1:
        st.header("column 1")
        with st.container(border=True):
            st.subheader("Deli Station")
            st.write("sandwich 1")
            st.write("sandwich 2")
            st.write("sandwich 3")
            st.write("sandwich 4")
            st.write("sandwich 5")
        with st.container(border=True):
            st.subheader("Pizza Station")
            st.write("pizza 1")
            st.write("pizza 2")
            st.write("pizza 3")
        with st.container(border=True):
            st.subheader("Grill Station")
            st.write("grill 1")
            st.write("grill 2")
            st.write("grill 3")



    with col2:
        st.header("column 2")
        st.subheader("Monday")
        st.write("**Sauté Station**")
        st.write("Option 1")
        st.write("Option 2")
        st.write("Option 3")
        st.write("---")

        st.subheader("Tuesday")
        st.write("**Sauté Station**")
        st.write("Option 1")
        st.write("Option 2")
        st.write("Option 3")
        st.write("---")

        st.subheader("Wednesday")
        st.write("**Sauté Station**")
        st.write("Option 1")
        st.write("Option 2")
        st.write("Option 3")
        st.write("---")

        st.subheader("Thursday")
        st.write("**Sauté Station**")
        st.write("Option 1")
        st.write("Option 2")
        st.write("Option 3")
        st.write("---")

        st.subheader("Friday")
        st.write("**Sauté Station**")
        st.write("Option 1")
        st.write("Option 2")
        st.write("Option 3")
        st.write("---")

elif week == "2":
    st.write("add info for week 2 here later")

elif week == "3":
    st.write("add info for week 3 here later")