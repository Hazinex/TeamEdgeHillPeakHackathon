# TeamEdgeHillPeakHackathon
This repository contains the code from the team "Team Edge Hill" used in the peak data science Hackathon 2024

## Analysing Data

### Task 1
Task 1 demonstrated the total sales and total profit for each product, category and sub-category. The findings are shown below:

- Canon imageCLASS 2200 Advanced Copier brought in the highest sales with a total of **184799.4720**. This also made the highest profit with **75599.7840**.
- Eureka Disposable Bags for Sanitaire Vibra Groomer I Upright Vac brought in the least sales with a total of **4.872**.
- Cubify CubeX 3D Printer Double Head Print resulted in the highest loss of **29279.9024**.
- Technology had the highest sales with **2678721**, followed by Furniture with **2422014** and then Office Supplies with **2320067**.
- Technology had the highest profit with **472045.5663**, followed by Office Supplies with **399637.2214** and then furniture with **60926.4669**.

### Task 3
the first section - purchase frequency is only half implemented
second section - order size for each customer section by product category has been created along with a graph, see below:

![PreferedCategories](https://github.com/Hazinex/TeamEdgeHillPeakHackathon/assets/91896453/14f24a77-f612-4368-b579-10f279fcf84d)

third section - creates a sum of all the orders within a specific customer segment and product category, this has been expressed in a bar chart, see below:

![QuantityBySegmentAndCategory](https://github.com/Hazinex/TeamEdgeHillPeakHackathon/assets/91896453/6f5e13a3-2894-4d1f-a79a-568e81d6aeb0)

## Forecasting

The model created used a multi-class Logistic Regression. The data was split 80:20, and chunk splitting was used to ensure that data was taken from a wide range of quantities.
```
