import streamlit as st
from streamlit_star_rating import st_star_rating

st.set_page_config(layout="wide")
st.title("Nutrition and Reviews")
st.write("---")
st.header("Turkey BLT")

col1, col2 = st.columns([0.4, 0.6])

with col1:
    with st.container(border=True):
        st.markdown(
            """
            <style>
            .nutrition-label {
                padding: 1em;
                font-family: Arial, sans-serif;
                font-size: 0.875em;
            }
            .nutrition-label h2 {
                font-size: 2.7em;
                margin: 0 0 0.625em 0;
                padding-bottom: 0.1em;
            }
            .nutrition-label .bold {
                font-weight: bold;
            }
            .horizontal-line {
                width: 100%;
                border: none;
                height: 0.2em;
                background-color: gray;
                margin: 0.625em 0;
            }
            </style>
            <div class="nutrition-label">
                <h2>Nutrition Facts</h2>
                <div class="horizontal-line"></div>
                <div><span class="bold">Serving Size:</span> 1 cup (228g)</div>
                <hl>
                <div><span class="bold">Servings Per Container:</span> 2</div>
                <div class="separator"></div>
                <div><span class="bold">Amount Per Serving</span></div>
                <div>
                    <span class="bold">Calories:</span> 200
                </div>
                <div class="separator"></div>
                <div>
                    <span class="bold">% Daily Value*</span>
                </div>
                <div>
                    <span class="bold">Total Fat</span> 8g <span class="bold">10%</span>
                </div>
                <div style="margin-left: 20px;">Saturated Fat 1g <span class="bold">5%</span></div>
                <div style="margin-left: 20px;">Trans Fat 0g</div>
                <div>
                    <span class="bold">Cholesterol</span> 30mg <span class="bold">10%</span>
                </div>
                <div>
                    <span class="bold">Sodium</span> 300mg <span class="bold">13%</span>
                </div>
                <div>
                    <span class="bold">Total Carbohydrate</span> 27g <span class="bold">9%</span>
                </div>
                <div style="margin-left: 20px;">Dietary Fiber 4g <span class="bold">14%</span></div>
                <div style="margin-left: 20px;">Total Sugars 12g</div>
                <div>
                    <span class="bold">Protein</span> 5g
                </div>
                <div class="separator"></div>
                <div>
                    Vitamin D 2mcg <span class="bold">10%</span> • Calcium 260mg <span class="bold">20%</span>
                </div>
                <div>
                    Iron 8mg <span class="bold">45%</span> • Potassium 235mg <span class="bold">6%</span>
                </div>
                <div class="separator"></div>
                <div style="font-size: 12px;">
                    *Percent Daily Values are based on a 2,000 calorie diet. Your daily values may be higher or lower depending on your calorie needs.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with st.container():
        if st.button("back"):
            st.switch_page("main.py")

with col2:
    with st.container():
        st.subheader("Leave a rating!")
        stars = st_star_rating(label="", maxValue=5, defaultValue=3, key="rating")
    with st.container(border=True):
        st.write("This sandwich is good")
    with st.container(border=True):
        st.write("Tasty!")
    with st.container(border=True):
        st.write("I didn't like this")