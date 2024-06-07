import os
from matplotlib import pyplot as plt
import pandas as pd 
from joblib import load, dump

def display_graph(df, title, xlbl, ylbl):
    df.plot(kind='bar')
    plt.title(title)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    plt.xticks(fontsize=8, wrap=True)
    plt.show()

# Loads the joblib
if os.path.exists("dataset.joblib"):
    dataset = load("dataset.joblib")
else:
    dataset = pd.read_excel("Superstore Dataset.xlsx", index_col=0)
    dump(dataset, "dataset.joblib")

# Takes the original dataframe and groups by the product name. The total sum and total profit is calculated for each product
# and is sorted from highest to lowest. Graphs are then displayed
products_sales = pd.DataFrame({'Sales': dataset.groupby('Product Name')['Sales'].sum()}).sort_values(by='Sales', ascending=False)
products_profit = pd.DataFrame({'Profit': dataset.groupby('Product Name')['Profit'].sum()}).sort_values(by='Profit', ascending=False)
display_graph(products_sales.head(10), "Top 10 Products for Total Sales", "Product", "Total Sales")
display_graph(products_sales.tail(10), "Worst 10 Products for Total Sales", "Product", "Total Sales")
display_graph(products_profit.head(10), "Top 10 Products for Total Profit", "Product", "Total Profit")
display_graph(products_profit.tail(10), "Worst 10 Products for Total Profit", "Product", "Total Profit")

# Takes the original dataframe and groups by the category. The total sum and total profit is calculated for each category
# and is sorted from highest to lowest. Graphs are then displayed
category_sales = pd.DataFrame({'Sales': dataset.groupby('Category')['Sales'].sum()}).sort_values(by='Sales', ascending=False)
category_profit = pd.DataFrame({'Profit': dataset.groupby('Category')['Profit'].sum()}).sort_values(by='Profit', ascending=False)
display_graph(category_sales, "Total Sales per Category", "Category", "Total Sales")
display_graph(category_profit, "Total Profit per Category", "Category", "Total Profit")

# Takes the original dataframe and groups by the sub category. The total sum and total profit is calculated for each sub category
# and is sorted from highest to lowest. Graphs are then displayed
subcategory_sales = pd.DataFrame({'Sales': dataset.groupby('Sub-Category')['Sales'].sum()}).sort_values(by='Sales', ascending=False)
subcategory_profit = pd.DataFrame({'Profit': dataset.groupby('Sub-Category')['Profit'].sum()}).sort_values(by='Profit', ascending=False)
display_graph(subcategory_sales, "Total Sales per Sub-Category", "Sub-Category", "Total Sales")
display_graph(subcategory_profit, "Total Profit per Sub-Category", "Sub-Category", "Total Profit")


