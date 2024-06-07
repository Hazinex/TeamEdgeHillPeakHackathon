import pandas as pd 
from datetime import date


class PromotionEffectiveness:
    def __init__(self, data_location):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        #load data
        self.data = pd.read_excel(data_location)
        #list of unique products
        self.unique_items = self.data["Product Name"].unique()
        #sord by product name
        self.grouped_name = self.data.sort_values("Product Name", axis=0)
        #product during promotion
        self.during_promotion = []
        #product after promotion
        self.after_promotion = []
        #product before promotion
        self.before_promotion = []
        #normal sales time
        self.normal_sale = []
        df = self.data.sort_values(by=["Product Name", "Order Date"], ascending=True)
        # print(df.iloc[:100, [2,16, 19]])
        current_product = ""
        promotion_date = 0
        for index, row in df.iterrows():
            if(index == len(self.data)-1):
                break
            #set current product
            if(current_product == ""):
                current_product = row["Product Name"]
            #during sale
            if(row["Discount"] > 0):
                self.during_promotion.append(row)
                promotion_date = row["Order Date"]
            #after sale
            elif(row["Discount"] == 0 and promotion_date != 0 and self.compare_date(promotion_date, row["Order Date"]) < 30):
                self.after_promotion.append(row)
            # #normal sale
            elif(row["Discount"] == 0 and promotion_date != 0 and self.compare_date(promotion_date, row["Order Date"]) > 30):
                self.normal_sale.append(row)
            #before sale
            elif(row["Discount"] == 0 and df.iloc[index+1]["Discount"] > 0 and self.compare_date(row["Order Date"], df.iloc[index+1]["Order Date"]) < 30):
                self.before_promotion.append(row)
            #before sale
            elif(row["Discount"] == 0 and df.iloc[index+1]["Discount"] > 0 and self.compare_date(row["Order Date"], df.iloc[index+1]["Order Date"]) > 30):
                self.normal_sale.append(row)
            #if new product reset promotion date 
            if(row["Product Name"] != current_product):
                current_product =  row["Product Name"]
                promotion = 0
            

            
        #during promotion sales data
        self.during_promotion = pd.DataFrame(self.during_promotion, columns=self.data.columns)
        #after promotion sales data
        self.after_promotion = pd.DataFrame(self.after_promotion, columns=self.data.columns)
        #before promotion sales data
        self.before_promotion = pd.DataFrame(self.before_promotion, columns=self.data.columns)
        #normal sales data 
        self.normal_sale = pd.DataFrame(self.normal_sale, columns=self.data.columns)

        quantity_results = []
        profit_results = []
        quantity_results.append(self.during_promotion.groupby("Product Name")["Quantity"].sum().values)
        quantity_results.append(self.after_promotion.groupby("Product Name")["Quantity"].sum().values)
        quantity_results.append(self.normal_sale.groupby("Product Name")["Quantity"].sum().values)
        quantity_results.append(self.before_promotion.groupby("Product Name")["Quantity"].sum().values)


        quantity_results = pd.DataFrame(quantity_results)
        # print(self.during_promotion.groupby("Product Name")["Profit"].sum())
        # print(self.after_promotion.groupby("Product Name")["Profit"].sum())
        # print(self.normal_sale.groupby("Product Name")["Profit"].sum())
        # print(self.before_promotion.groupby("Product Name")["Profit"].sum())
        

    def compare_date(self, date_a, date_b):
        d0 = date_a.to_pydatetime() #date 1
        d1 = date_b.to_pydatetime() # date 2
        delta = d1 - d0 # find difference
        return delta.days #number of days



PromotionEffectiveness("../../Superstore Dataset.xlsx")
