import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("data/gpi_2025-26.csv")

# Calculate GPI
df["GPI"] = (df["sec_girls"] / df["sec_boys"]).round(4)

# Dashboard title
st.title("Gender Parity Index Dashboard")
st.write("Academic Year: 2025-26")

# State selector
state = st.selectbox("Select State", df["state"])
data = df[df["state"] == state].iloc[0]

# Display metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Boys", int(data["sec_boys"]))
col2.metric("Girls", int(data["sec_girls"]))
col3.metric("Total Students", int(data["sec_boys"] + data["sec_girls"]))
col4.metric("GPI", data["GPI"])

if data["GPI"] > 1:
    st.success("Girls' enrolment is higher than boys' enrolment.")
elif data["GPI"] < 1:
    st.info("Boys' enrolment is higher than girls' enrolment.")
else:  
    st.success("Girls' and boys' enrolment are equal.")

# Bar chart
st.subheader("Boys vs Girls Enrolment")

chart = pd.DataFrame({
    "Gender": ["Boys", "Girls"],
    "Students": [data["sec_boys"], data["sec_girls"]]
})

st.bar_chart(chart.set_index("Gender"))

# Display data
st.subheader("State Data")
st.dataframe(df)