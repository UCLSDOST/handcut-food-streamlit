import streamlit as st

st.set_page_config(layout="wide")

st.title('Menu (Mock)')
st.write("---")

week1 = "This week" #week of 9/2
week2 = "Week of 9/9"
week3 = "Week of 9/16"

week = st.selectbox(
    "Select Week",
    (week1, week2, week3)
)

if week == week1:
    with st.container(border=True):
        st.write("Allergen Guide: put info here for vegan / gf etc")

    col1, col2 = st.columns(spec=[0.4, 0.6])

    # menu that doesn't change
    with col1:
        with st.container(border=True):
            st.subheader(":orange[Deli Station]")
            st.write("Turkey BLT")
            st.write("Muffaletta Sandwich")
            st.write("Caprese")
            st.write("Ham & Swiss")
            st.write("Tuna Salad")
            st.write("Grilled Vegetable Ciabatta")
            st.write("Build Your Own")
        with st.container(border=True):
            st.subheader(":orange[Pizza Station]")
            st.write("Cheese")
            st.write("Pepperoni or Sausage")
            st.write("Veggie")
        with st.container(border=True):
            st.subheader(":orange[Grill Station]")
            st.write("Grilled Cheese")
            st.write("Chicken Tenders")
            st.write("Cheeseburgers")
            st.write("Hot Dogs")
            st.write("Seasoned Fries")
            st.write("Sweet Potato Fries")

    # weekly menu
    with col2:

        #day and menu
        st.subheader(":orange[Monday]")
        st.write("""
        **Sauté Station**
        <br>
        Teriyaki Chicken Stir Fry (S) or Fried Tofu (S)
        <br> 
        Peas, Cabbage & Peppers
        <br> 
        Steamed Jasmine Rice
        """, unsafe_allow_html=True)

        innercol1, innercol2 = st.columns(2)
        with innercol1:
            st.write("""
            **Vegetable**
            <br>
            **Sandwich**
            <br>
            **Salad Bar**
            <br>
            **Breakfast**
            """, unsafe_allow_html=True)
        with innercol2:
            st.write("""
            Greek Green Beans
            <br>
            Italian Beef with Peppers & Onions (G, W)
            <br>
            Rotating selection of Greens, Veggies, Proteins & Toppings
            <br>
            Eggs or Eggs & Chorizo (E), Jalapeno Breakfast Potatoes & Tortillas
            """, unsafe_allow_html=True)
        st.write("---")

        # tuesday
        st.subheader(":orange[Tuesday]")
        st.write("""
        **Sauté Station**
        <br>
        Teriyaki Chicken Stir Fry (S) or Fried Tofu (S)
        <br> 
        Peas, Cabbage & Peppers
        <br> 
        Steamed Jasmine Rice
        """, unsafe_allow_html=True)

        innercol1, innercol2 = st.columns(2)
        with innercol1:
            st.write("""
            **Vegetable**
            <br>
            **Sandwich**
            <br>
            **Salad Bar**
            <br>
            **Breakfast**
            """, unsafe_allow_html=True)
        with innercol2:
            st.write("""
            Greek Green Beans
            <br>
            Italian Beef with Peppers & Onions (G, W)
            <br>
            Rotating selection of Greens, Veggies, Proteins & Toppings
            <br>
            Eggs or Eggs & Chorizo (E), Jalapeno Breakfast Potatoes & Tortillas
            """, unsafe_allow_html=True)
        st.write("---")

        # wednesday
        st.subheader(":orange[Wednesday]")
        st.write("""
        **Sauté Station**
        <br>
        Teriyaki Chicken Stir Fry (S) or Fried Tofu (S)
        <br> 
        Peas, Cabbage & Peppers
        <br> 
        Steamed Jasmine Rice
        """, unsafe_allow_html=True)

        innercol1, innercol2 = st.columns(2)
        with innercol1:
            st.write("""
            **Vegetable**
            <br>
            **Sandwich**
            <br>
            **Salad Bar**
            <br>
            **Breakfast**
            """, unsafe_allow_html=True)
        with innercol2:
            st.write("""
            Greek Green Beans
            <br>
            Italian Beef with Peppers & Onions (G, W)
            <br>
            Rotating selection of Greens, Veggies, Proteins & Toppings
            <br>
            Eggs or Eggs & Chorizo (E), Jalapeno Breakfast Potatoes & Tortillas
            """, unsafe_allow_html=True)
        st.write("---")

        # thursday
        st.subheader(":orange[Thursday]")
        st.write("""
        **Sauté Station**
        <br>
        Teriyaki Chicken Stir Fry (S) or Fried Tofu (S)
        <br> 
        Peas, Cabbage & Peppers
        <br> 
        Steamed Jasmine Rice
        """, unsafe_allow_html=True)

        innercol1, innercol2 = st.columns(2)
        with innercol1:
            st.write("""
            **Vegetable**
            <br>
            **Sandwich**
            <br>
            **Salad Bar**
            <br>
            **Breakfast**
            """, unsafe_allow_html=True)
        with innercol2:
            st.write("""
            Greek Green Beans
            <br>
            Italian Beef with Peppers & Onions (G, W)
            <br>
            Rotating selection of Greens, Veggies, Proteins & Toppings
            <br>
            Eggs or Eggs & Chorizo (E), Jalapeno Breakfast Potatoes & Tortillas
            """, unsafe_allow_html=True)
        st.write("---")

        # friday
        st.subheader(":orange[Friday]")
        st.write("""
        **Sauté Station**
        <br>
        Teriyaki Chicken Stir Fry (S) or Fried Tofu (S)
        <br> 
        Peas, Cabbage & Peppers
        <br> 
        Steamed Jasmine Rice
        """, unsafe_allow_html=True)

        innercol1, innercol2 = st.columns(2)
        with innercol1:
            st.write("""
            **Vegetable**
            <br>
            **Sandwich**
            <br>
            **Salad Bar**
            <br>
            **Breakfast**
            """, unsafe_allow_html=True)
        with innercol2:
            st.write("""
            Greek Green Beans
            <br>
            Italian Beef with Peppers & Onions (G, W)
            <br>
            Rotating selection of Greens, Veggies, Proteins & Toppings
            <br>
            Eggs or Eggs & Chorizo (E), Jalapeno Breakfast Potatoes & Tortillas
            """, unsafe_allow_html=True)
        st.write("---")


elif week == week2:
    st.header("Coming soon!")

elif week == week3:
    st.header("Coming soon!")