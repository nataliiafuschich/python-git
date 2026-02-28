
def total_sales_by_city(df):
    return df.groupby("city")["sales"].sum()

def average_sales_by_city(df):
    return df.groupby("city")["sales"].mean()
