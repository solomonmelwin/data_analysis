#importing libraries
import pandas as pd

#loading dataset
print("loading dataset")
df = pd.read_csv("data/sales.csv")
print("dataset loaded sucessfully")

#data inspection
print("data inspection")

print("#sample dataset: \n",df.head())
print("#data information:")
df.info()
print("# columns in dataset: \n",df.columns)
print("#about numerical data :\n",df.describe())
print("#about all kind: \n",df.describe(include='all'))

#data summary

print("#total sales report: \n","total_sales:",round(df["total_bill"].sum(),2))
print("#average sales report: \n","average_sales:",round(df["total_bill"].mean(),2))
print("#total orders recieved: \n","total_orders:",len(df))

#data cleaning and analysis

print("data cleaning and analysing begins")
print("#checking null values:\n",df.isnull().sum())
print("#checking the data types: \n",df.dtypes)
#creating new column for bill per person
df["bill_per_person"]=df["total_bill"]/df["size"]
print(df.head(),"\n #new column bill per person created sucessfully")

# data insights
print("Data Insights")

sales_by_day =df.groupby("day")["total_bill"].sum()
print("#sales with respective day Insights: \n",sales_by_day)
sales_by_time =df.groupby("time")["total_bill"].sum()
print("#sales with respective time insights: \n",sales_by_time)

#visualization of insights

print("visualization Insights")

print("importing packages (seaborn) and (matplotlib)")

import matplotlib.pyplot as plt
import seaborn as sns

print("sales by day chart")

sales_by_day.plot(kind="bar")
plt.title("sales by day")
plt.xlabel("Day")
plt.ylabel("Total revenue")
plt.savefig("sales_by_day.png")
plt.show()

print("sales by time chart")
sales_by_time.plot(kind="bar",color="orange")
plt.title("sales by time")
plt.xlabel("Time")
plt.ylabel("Total Revenue")
plt.savefig("sales_by_time.png")
plt.show()

print("bill distribution")
sns.set_style("whitegrid")
sns.histplot(df["total_bill"],bins=20)
plt.title("Distribution of total bill")
plt.savefig("bill_distribution.png")
plt.show()