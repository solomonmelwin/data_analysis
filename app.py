import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Business sales dashboard", layout="wide")

st.header("Executive Summary")
st.divider()

st.title("Business Performance Dashboard")

st.markdown("Analyze Sales, Profit, and Customer Trends.")

df=pd.read_csv("data/superstore.CSV",encoding="latin-1")

st.sidebar.header("Filters")

region = st.sidebar.multiselect("Select Region", df["Region"].unique(),default=df["Region"].unique())
filtered_df =df[df["Region"].isin(region)]
total_sales =filtered_df["Sales"].sum()
total_profit =filtered_df["Profit"].sum()
total_orders=len(filtered_df)

col1,col2,col3 =st.columns(3)

col1.metric("Total Sales",f"${total_sales:,.0f}")
col2.metric("Total Profit",f"${total_profit:,.0f}")
col3.metric("Total Orders",total_orders)

sales_by_region = filtered_df.groupby("Region")["Sales"].sum()

fig, ax =plt.subplots()
sales_by_region.plot(kind="bar", ax=ax)
ax.set_xlabel("Region")
ax.set_ylabel("Total Sales")
ax.set_title("Sales by Region")
st.pyplot(fig)

profit_by_category =filtered_df.groupby("Category")["Profit"].sum()
fig2 , ax2 =plt.subplots()
profit_by_category.plot(kind="bar", ax=ax2,color="orange")
ax2.set_xlabel("Category")
ax2.set_ylabel("Total Profit")
ax2.set_title("Profit by Category")
st.pyplot(fig2)

top_customers=(filtered_df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10))

st.subheader("Top 10 Customers by Sales")
st.dataframe(top_customers)

monthly_sales =df.groupby("Order Date")["Sales"].sum()
st.line_chart(monthly_sales)
st.subheader("Buisness Insights")

st.write("""
- The West region shows strong sales performance.
- Some categories generate high sales but low profit. 
- Top customers contribute significantly to revenue. 
""")

st.subheader("Recommendations")
st.write("""
- Increase focus on high-profit Categories.
- Reduce excessive discounts on low-margin products.
- Target performing Regions with Promotions.
- Improve performance in weaker sales months.
""")

st.success("Dashboard loaded successfully!")