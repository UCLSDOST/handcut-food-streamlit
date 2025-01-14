import streamlit as st
from streamlit_star_rating import st_star_rating

menu_item = st.session_state.menu_items[st.session_state["menu_item"]]

st.set_page_config(layout="wide")
st.title("Nutrition and Reviews")
st.write("---")
st.header(menu_item["name"])

col1, col2 = st.columns([0.4, 0.6])

with col1:
    with st.container(border=True):
        st.write(
            """
            <style>

.performance-facts {
  font-size: small;
            line-height: 1.4;
            color: black;
  border: 1px solid black;
  background: white;
  margin: 20px;
  float: left;
  width: 335px;
  padding: 0.5rem;
  table {
    border-collapse: collapse;
  }
}
.performance-facts__title {
  font-weight: bold;
  font-size: 2rem;
  margin: 0;
  padding: 0;
  h1 {
            padding: 0 !important;
            }
}
            
.performance-facts__header {
  border-bottom: 10px solid black;
  padding: 0;
  margin: 0;
  p {
    margin: 0;
  }
}
           .performance-facts p {
            margin: 0px;
            }

.performance-facts__table {
  width: 100%;
  thead tr {
    th,
    td {
      border: 0;
    }
  }
  th,
  td {
    font-weight: normal;
    text-align: left;
    padding: 0.25rem 0;
    border-top: 0.1rem solid black;
    white-space: nowrap;
  }
  td {
    &:last-child {
      text-align: right;
    }
  }
  .blank-cell {
    width: 1rem;
    border-top: 0;
  }
  .thick-row {
    th,
    td {
      border-top-width: 5px;
    }
  }
}
.small-info {
  font-size: 0.7rem;
}

.performance-facts__table--small {
  @extend .performance-facts__table;
  border-bottom: 1px solid #999;
  margin: 0 0 0.5rem 0;
  thead {
    tr {
      border-bottom: 1px solid black;
    }
  }
  td {
    &:last-child {
      text-align: left;
    }
  }
  th,
  td {
    border: 0;
    padding: 0;
  }
}

.performance-facts__table--grid {
  @extend .performance-facts__table;
  margin: 0 0 0.5rem 0;
  td {
    &:last-child {
      text-align: left;
      &::before {
        content: "•";
        font-weight: bold;
        margin: 0 0.25rem 0 0;
      }
    }
  }
}

.text-center {
  text-align: center;
}
.thick-end {
  border-bottom: 10px solid black;
}
.thin-end {
  border-bottom: 1px solid black;
}
            </style>

            """,
            unsafe_allow_html = True)
        st.markdown(
            f"""

<section class="performance-facts">
  <header class="performance-facts__header">
    <h1 class="performance-facts__title", style="padding:0;">Nutrition Facts</h1>
    <p>Serving Size 1/2 cup (about 82g)
      <p>Serving Per Container 8</p>
  </header>
  <table class="performance-facts__table">
    <thead>
      <tr>
        <th colspan="3" class="small-info">
          Amount Per Serving
        </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th colspan="2">
          <b>Calories</b>
          200
        </th>
        <td>
          Calories from Fat
          130
        </td>
      </tr>
      <tr class="thick-row">
        <td colspan="3" class="small-info">
          <b>% Daily Value*</b>
        </td>
      </tr>
      <tr>
        <th colspan="2">
          <b>Total Fat</b>
          14g
        </th>
        <td>
          <b>22%</b>
        </td>
      </tr>
      <tr>
        <td class="blank-cell">
        </td>
        <th>
          Saturated Fat
          9g
        </th>
        <td>
          <b>22%</b>
        </td>
      </tr>
      <tr>
        <td class="blank-cell">
        </td>
        <th>
          Trans Fat
          0g
        </th>
        <td>
        </td>
      </tr>
      <tr>
        <th colspan="2">
          <b>Cholesterol</b>
          55mg
        </th>
        <td>
          <b>18%</b>
        </td>
      </tr>
      <tr>
        <th colspan="2">
          <b>Sodium</b>
          40mg
        </th>
        <td>
          <b>2%</b>
        </td>
      </tr>
      <tr>
        <th colspan="2">
          <b>Total Carbohydrate</b>
          17g
        </th>
        <td>
          <b>6%</b>
        </td>
      </tr>
      <tr>
        <td class="blank-cell">
        </td>
        <th>
          Dietary Fiber
          1g
        </th>
        <td>
          <b>4%</b>
        </td>
      </tr>
      <tr>
        <td class="blank-cell">
        </td>
        <th>
          Sugars
          14g
        </th>
        <td>
        </td>
      </tr>
      <tr class="thick-end">
        <th colspan="2">
          <b>Protein</b>
          3g
        </th>
        <td>
        </td>
      </tr>
    </tbody>
  </table>


  <p class="small-info">* Percent Daily Values are based on a 2,000 calorie diet. Your daily values may be higher or lower depending on your calorie needs:</p>
</section>
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
