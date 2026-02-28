import pandas as pd

def load_data():
    data = {
        "city": ["Kyiv", "Lviv", "Odesa", "Kyiv", "Lviv", "Odesa"],
        "month": ["Jan", "Jan", "Jan", "Feb", "Feb", "Feb"],
        "sales": [1200, 900, 500, 1500, 1100, 700]
    }
    return pd.DataFrame(data)
