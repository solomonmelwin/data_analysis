import streamlit as st
import pandas as pd

st.markdown("<h1 style='text-align: center;'>Restaurant Sales Dashboard</h1>", unsafe_allow_html=True)

df =pd.read_csv("data/sales.csv")

with st.expander("View Sample Data"):
    st.dataframe(df.head())

st.write("## Insights")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sales", f"${round(df["total_bill"].sum(), 2)}")

with col2:
    st.metric("Average Sales", f"${round(df["total_bill"].mean(), 2)}")

with col3:
    st.metric("Total Orders", len(df))

st.markdown("---")

st.markdown("## 📊 Sales Insights")

sales_by_day = df.groupby("day")["total_bill"].sum()
sales_by_time = df.groupby("time")["total_bill"].sum()
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
sns.set_palette("Set2")  # nice soft colors

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(6,4))

    sales_by_day.plot(kind="bar", ax=ax, color="skyblue")

    ax.set_title("📊 Weekly Sales Performance", fontsize=14)
    ax.set_xlabel("Day")
    ax.set_ylabel("Revenue")

    # Add value labels on top
    for i, v in enumerate(sales_by_day):
        ax.text(i, v + 10, str(round(v, 1)), ha='center')

    st.pyplot(fig)
with col2:
    fig, ax = plt.subplots(figsize=(6,4))

    sales_by_time.plot(kind="bar", ax=ax, color="orange")

    ax.set_title("⏰ Revenue: Lunch vs Dinner", fontsize=14)
    ax.set_xlabel("Time")
    ax.set_ylabel("Revenue")

    for i, v in enumerate(sales_by_time):
        ax.text(i, v + 10, str(round(v, 1)), ha='center')

    st.pyplot(fig)

st.markdown("---")


st.markdown("## 📈 Customer Behavior")

fig, ax = plt.subplots()

sns.histplot(df["total_bill"], bins=20, kde=True, color="purple", ax=ax)

ax.set_title("Distribution of Customer Spending")
ax.set_xlabel("Bill Amount")
ax.set_ylabel("Number of Orders")

st.pyplot(fig)

st.markdown("---") 

st.markdown("## Buisness Insights")


st.info("💡 Most sales happen on weekends, especially Saturday and Sunday.")

st.info("💡 Dinner generates significantly more revenue than lunch.")

st.info("💡 Most customers spend between 10–25, indicating mid-range pricing.")


st.success("📈 Peak sales occur during dinner time and weekends.")

st.caption("Built using Python + Streamlit | Data Analytics Dashboard with Business Insights")