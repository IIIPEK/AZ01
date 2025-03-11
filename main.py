import pandas as pd

def df_info(df):
    print("*** Head 5 rows:\n", df.head())
    print("*** Tail 5 rows:\n", df.tail())
    print("*** Columns:\n", df.columns)
    print("*** Info:\n", df.info())
    print("*** Describe:\n", df.describe())
    print("*** Dtypes:\n", df.dtypes)
    print("*** Shape:\n", df.shape)
    print("*** Null:\n", df.isnull().sum())
    print("*** Null sum:\n", df.isnull().sum().sum())
    print("*** NaN:\n", df.isna().sum())
    print("*** NaN sum:\n", df.isna().sum().sum())


df = pd.read_csv("car_price_dataset.csv")
df_info(df)

print(round(df.groupby("Brand")["Price"].mean(),2))

print("\n############# Вторая часть ############")

df = pd.read_csv("dz.csv")

print(df.groupby("City")["Salary"].mean())

