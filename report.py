from data import load_data
from analysis import total_sales_by_city

df = load_data()
result = total_sales_by_city(df)
print("Загальні продажі по містах:")
print(result)
